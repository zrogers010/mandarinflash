from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('autocomplete-items/', views.autocomplete_items, name='autocomplete_items'),
    path('character/<str:char>', views.character, name="character"),
    # path('hsk1', views.hsk1_flash, name="hsk1"),
    # path('hsk2', views.hsk2_flash, name="hsk2"),
    # path('hsk3', views.hsk3_flash, name="hsk3"),
    # path('hsk4', views.hsk4_flash, name="hsk4"),
    # path('hsk5', views.hsk5_flash, name="hsk5"),
    # path('hsk6', views.hsk6_flash, name="hsk6"),
    # path('hsk1/words', views.hsk1_words, name="hsk1_words"),
    # path('hsk2/words', views.hsk2_words, name="hsk2_words"),
    # path('hsk3/words', views.hsk3_words, name="hsk3_words"),
    # path('hsk4/words', views.hsk4_words, name="hsk4_words"),
    # path('hsk5/words', views.hsk5_words, name="hsk5_words"),
    # path('hsk6/words', views.hsk6_words, name="hsk6_words"),
    path('quiz/<int:level>', views.flashcards, name="flashcards"),
    path('words/<int:level>', views.wordslist, name="wordslist"),
    path('flashcards/<int:level>/new_words/', views.new_flashcard_words, name='new_flashcard_words'),
]
