from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('autocomplete-items/', views.autocomplete_items, name='autocomplete_items'),
    path('character/<str:char>', views.character, name="character"),
    path('quiz/<int:level>', views.flashcards, name="flashcards"),
    path('words/<int:level>', views.wordslist, name="wordslist"),
]
