"""Маршруты (URL) для приложения countries."""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz/', views.quiz_view, name='quiz'),
    path('quiz/finish/', views.quiz_finish, name='quiz_finish'),
    path('list/', views.country_list, name='list'),
    path('add/', views.add_country, name='add_country'),
    path('edit/<int:country_id>/', views.edit_country, name='edit'),
    path('delete/<int:country_id>/', views.delete_country, name='delete_country'),
    path('toggle/<int:country_id>/', views.toggle_learned, name='toggle_learned'),
    path('flashcards/', views.flashcards, name='flashcards'),
]
