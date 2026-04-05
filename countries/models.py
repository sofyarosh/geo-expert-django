"""Модели данных для приложения GeoExpert."""
from django.db import models

class Country(models.Model):
    """Модель, представляющая страну и её характеристики."""
    CONTINENT_CHOICES = [
        ('Европа', 'Европа'),
        ('Азия', 'Азия'),
        ('Африка', 'Африка'),
        ('Северная Америка', 'Северная Америка'),
        ('Южная Америка', 'Южная Америка'),
        ('Океания', 'Океания'),
    ]

    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    capital = models.CharField(max_length=150, verbose_name="Столица")
    flag_url = models.URLField(max_length=500, verbose_name="Ссылка на флаг")
    continent = models.CharField(
        max_length=50,
        choices=CONTINENT_CHOICES,
        default='Европа',
        verbose_name="Материк"
    )
    is_learned = models.BooleanField(default=False, verbose_name="Выучено")
    notes = models.TextField(blank=True, verbose_name="Заметки")

    def __str__(self):
        return str(self.name)

class QuizResult(models.Model):
    """Модель для хранения результатов игровых раундов."""
    player_name = models.CharField(max_length=100)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player_name} - {self.score}"
        