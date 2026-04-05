"""
GeoExpert: Логика образовательного тренажера.
Обработка списков стран, прогресса и игровых сессий.
"""

import random
from django.shortcuts import render, redirect, get_object_or_404
from .models import Country, QuizResult
from .forms import CapitalForm, CountryForm

def index(request):
    """Главная страница с выбором региона и историей игр."""
    continents = ['Европа', 'Азия', 'Африка', 'Северная Америка', 'Южная Америка', 'Океания']
    results = QuizResult.objects.all().order_by('-date')[:5]
    return render(request, 'countries/index.html', {
        'continents': continents,
        'results': results
    })

def country_list(request):
    """Список всех стран и расчет прогресса пользователя."""
    all_countries = Country.objects.all().order_by('name')
    total = all_countries.count()
    learned = all_countries.filter(is_learned=True).count()
    percentage = int((learned / total) * 100) if total > 0 else 0
    return render(request, 'countries/list.html', {
        'countries': all_countries,
        'learned': learned,
        'total': total,
        'percentage': percentage
    })

def quiz_view(request):
    """Основная логика квиза с защитой от ошибок сессии и сбросом режимов."""
    continent_param = request.GET.get('continent')


    if continent_param:
        request.session['selected_continent'] = None if continent_param == 'all' else continent_param
        request.session['is_playing'] = False
        request.session['quiz_score'] = 0
        request.session['mistakes'] = []
        request.session['seen_ids'] = []
        request.session['current_id'] = None
        request.session['last_was_correct'] = None


    if not request.session.get('is_playing'):
        sel_cont = request.session.get('selected_continent')
        queryset = Country.objects.filter(continent=sel_cont) if sel_cont else Country.objects.all()
        if request.method == 'POST':
            request.session['is_playing'] = True
            return redirect('quiz')
        return render(request, 'countries/quiz_start.html', {
            'continent': sel_cont or "Все страны",
            'count': queryset.count()
        })

    state = request.GET.get('state', 'question')
    curr_id = request.session.get('current_id')
    mistakes = request.session.get('mistakes', [])


    if curr_id:
        target = get_object_or_404(Country, id=curr_id)
        is_skip = (state == 'next' and request.session.get('last_was_correct') != curr_id)
        if state == 'reveal' or is_skip:
            if not any(m['name'] == target.name for m in mistakes):
                mistakes.append({'name': target.name, 'capital': target.capital, 'flag': target.flag_url})
                request.session['mistakes'] = mistakes

 
    if not curr_id or state == 'next':
        if curr_id:
            seen = request.session.get('seen_ids', [])
            if curr_id not in seen:
                seen.append(curr_id)
                request.session['seen_ids'] = seen

        sel_cont = request.session.get('selected_continent')
        qs = Country.objects.filter(continent=sel_cont) if sel_cont else Country.objects.all()
        remaining = qs.exclude(id__in=request.session.get('seen_ids', []))

        if not remaining.exists():
            return redirect('quiz_finish')

        new_target = random.choice(remaining)
        request.session['current_id'] = new_target.id
        request.session['last_was_correct'] = None
        return redirect('quiz')


    target = get_object_or_404(Country, id=curr_id)
    form = CapitalForm(request.POST or None)

    if request.method == 'POST' and state == 'question':
        if form.is_valid():
            if form.cleaned_data['answer'].strip().lower() == target.capital.lower():
                request.session['quiz_score'] = request.session.get('quiz_score', 0) + 1
                request.session['last_was_correct'] = target.id
                return render(request, 'countries/quiz.html', {'country': target, 'state': 'correct', 'form': form})
            
            if not any(m['name'] == target.name for m in mistakes):
                mistakes.append({'name': target.name, 'capital': target.capital, 'flag': target.flag_url})
                request.session['mistakes'] = mistakes
            form.add_error('answer', 'Неверно, попробуйте еще раз!')

    return render(request, 'countries/quiz.html', {
        'country': target, 'form': form, 'state': state, 
        'score': request.session.get('quiz_score', 0)
    })

def quiz_finish(request):
    """Отображение итогов и очистка данных сессии."""
    if 'is_playing' in request.session:
        data = {
            'score': request.session.get('quiz_score', 0),
            'total': len(request.session.get('seen_ids', [])),
            'mistakes': request.session.get('mistakes', [])
        }
        QuizResult.objects.create(player_name="Ученик", score=data['score'])
        request.session.flush()
        return render(request, 'countries/quiz_summary.html', data)
    return redirect('index')

def add_country(request):
    """Добавление новой страны в базу данных."""
    form = CountryForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('list')
    return render(request, 'countries/edit.html', {'form': form, 'title': 'Новая страна'})

def edit_country(request, country_id):
    """Редактирование данных существующей страны."""
    country = get_object_or_404(Country, id=country_id)
    form = CountryForm(request.POST or None, instance=country)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('list')
    return render(request, 'countries/edit.html', {'form': form, 'country': country})

def delete_country(_request, country_id):
    """Удаление страны из базы."""
    get_object_or_404(Country, id=country_id).delete()
    return redirect('list')

def toggle_learned(_request, country_id):
    """Переключение статуса 'Выучено'."""
    country = get_object_or_404(Country, id=country_id)
    country.is_learned = not country.is_learned
    country.save()
    return redirect('list')

def flashcards(request):
    """Страница с карточками Anki для запоминания."""
    return render(request, 'countries/flashcards.html', {
        'countries': Country.objects.all().order_by('?')
    })
