import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from countries.models import Country

data = [
    # ЕВРОПА
    {"name": "Франция", "capital": "Париж", "continent": "Европа", "flag_url": "https://flagcdn.com/w640/fr.png"},
    {"name": "Германия", "capital": "Берлин", "continent": "Европа", "flag_url": "https://flagcdn.com/w640/de.png"},
    {"name": "Италия", "capital": "Рим", "continent": "Европа", "flag_url": "https://flagcdn.com/w640/it.png"},
    {"name": "Испания", "capital": "Мадрид", "continent": "Европа", "flag_url": "https://flagcdn.com/w640/es.png"},
    {"name": "Великобритания", "capital": "Лондон", "continent": "Европа", "flag_url": "https://flagcdn.com/w640/gb.png"},

    # АЗИЯ
    {"name": "Япония", "capital": "Токио", "continent": "Азия", "flag_url": "https://flagcdn.com/w640/jp.png"},
    {"name": "Китай", "capital": "Пекин", "continent": "Азия", "flag_url": "https://flagcdn.com/w640/cn.png"},
    {"name": "Индия", "capital": "Нью-Дели", "continent": "Азия", "flag_url": "https://flagcdn.com/w640/in.png"},
    {"name": "Южная Корея", "capital": "Сеул", "continent": "Азия", "flag_url": "https://flagcdn.com/w640/kr.png"},
    {"name": "Таиланд", "capital": "Бангкок", "continent": "Азия", "flag_url": "https://flagcdn.com/w640/th.png"},

    # АФРИКА
    {"name": "Египет", "capital": "Каир", "continent": "Африка", "flag_url": "https://flagcdn.com/w640/eg.png"},
    {"name": "ЮАР", "capital": "Претория", "continent": "Африка", "flag_url": "https://flagcdn.com/w640/za.png"},
    {"name": "Нигерия", "capital": "Абуджа", "continent": "Африка", "flag_url": "https://flagcdn.com/w640/ng.png"},
    {"name": "Марокко", "capital": "Рабат", "continent": "Африка", "flag_url": "https://flagcdn.com/w640/ma.png"},
    {"name": "Кения", "capital": "Найроби", "continent": "Африка", "flag_url": "https://flagcdn.com/w640/ke.png"},

    # СЕВЕРНАЯ АМЕРИКА
    {"name": "США", "capital": "Вашингтон", "continent": "Северная Америка", "flag_url": "https://flagcdn.com/w640/us.png"},
    {"name": "Канада", "capital": "Оттава", "continent": "Северная Америка", "flag_url": "https://flagcdn.com/w640/ca.png"},
    {"name": "Мексика", "capital": "Мехико", "continent": "Северная Америка", "flag_url": "https://flagcdn.com/w640/mx.png"},
    {"name": "Куба", "capital": "Гавана", "continent": "Северная Америка", "flag_url": "https://flagcdn.com/w640/cu.png"},
    {"name": "Панама", "capital": "Панама", "continent": "Северная Америка", "flag_url": "https://flagcdn.com/w640/pa.png"},

    # ЮЖНАЯ АМЕРИКА
    {"name": "Бразилия", "capital": "Бразилиа", "continent": "Южная Америка", "flag_url": "https://flagcdn.com/w640/br.png"},
    {"name": "Аргентина", "capital": "Буэнос-Айрес", "continent": "Южная Америка", "flag_url": "https://flagcdn.com/w640/ar.png"},
    {"name": "Колумбия", "capital": "Богота", "continent": "Южная Америка", "flag_url": "https://flagcdn.com/w640/co.png"},
    {"name": "Перу", "capital": "Лима", "continent": "Южная Америка", "flag_url": "https://flagcdn.com/w640/pe.png"},
    {"name": "Чили", "capital": "Сантьяго", "continent": "Южная Америка", "flag_url": "https://flagcdn.com/w640/cl.png"},

    # ОКЕАНИЯ
    {"name": "Австралия", "capital": "Канберра", "continent": "Океания", "flag_url": "https://flagcdn.com/w640/au.png"},
    {"name": "Новая Зеландия", "capital": "Веллингтон", "continent": "Океания", "flag_url": "https://flagcdn.com/w640/nz.png"},
    {"name": "Фиджи", "capital": "Сува", "continent": "Океания", "flag_url": "https://flagcdn.com/w640/fj.png"},
    {"name": "Папуа — Новая Гвинея", "capital": "Порт-Морсби", "continent": "Океания", "flag_url": "https://flagcdn.com/w640/pg.png"},
    {"name": "Самоа", "capital": "Апиа", "continent": "Океания", "flag_url": "https://flagcdn.com/w640/ws.png"},
]

def fill_db():
    Country.objects.all().delete()
    for item in data:
        Country.objects.create(**item)
    print(f"База успешно наполнена! Добавлено {Country.objects.count()} стран.")

if __name__ == "__main__":
    fill_db()
