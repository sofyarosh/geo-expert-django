"""Настройки административной панели для приложения countries."""
from django.contrib import admin
from .models import Country, QuizResult

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """Настройка отображения стран в админке."""
    list_display = ('name', 'capital', 'is_learned')
    list_filter = ('is_learned', 'continent')

@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    """Настройка отображения результатов в админке."""
    list_display = ('player_name', 'score', 'date')
    