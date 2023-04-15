from django.urls import path, re_path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
 
urlpatterns = [
        path("save_quiz_scores/", views.save_quiz_scores, name="save_quiz_scores"),
]