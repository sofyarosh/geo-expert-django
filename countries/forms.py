"""Формы для управления данными стран и проведения квиза."""
from django import forms
from .models import Country

class CapitalForm(forms.Form):
    """Форма для ввода ответа в квизе."""
    answer = forms.CharField(label="Введите столицу", max_length=100)

    def clean_answer(self):
        """Проверка на отсутствие цифр в названии столицы."""
        answer = self.cleaned_data.get('answer')
        if any(char.isdigit() for char in answer):
            raise forms.ValidationError("Цифры в названии недопустимы!")
        return answer

class CountryForm(forms.ModelForm):
    """Универсальная форма для создания и редактирования стран с валидацией."""
    class Meta:
        """Настройки формы."""
        model = Country
        fields = ['name', 'capital', 'flag_url', 'continent', 'is_learned', 'notes']

    def clean_name(self):
        """Проверка, что в названии страны нет цифр."""
        name = self.cleaned_data.get('name')
        if any(char.isdigit() for char in name):
            raise forms.ValidationError("Название страны не может содержать цифры!")
        return name

    def clean_capital(self):
        """Проверка, что в названии столицы нет цифр."""
        capital = self.cleaned_data.get('capital')
        if any(char.isdigit() for char in capital):
            raise forms.ValidationError("Название столицы не может содержать цифры!")
        return capital
        
