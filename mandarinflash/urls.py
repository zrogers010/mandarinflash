from django.contrib import admin
from django.urls import path, re_path, include
import api
from api import views as api_view
from chatbot import views as chatbot_view
from user import views as user_view
from website import views as website_view
from django.contrib.auth import views as auth

regex_pattern = '(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('api/', include('api.urls')),
    #path('activate/<str:uidb64>/<str:token>/', user_view.activate, name='activate'),
    re_path(r'^activate/{}/$'.format(regex_pattern), user_view.activate, name='activate'),  
    path('login/', user_view.login_request, name ='login'),
    path('logout/', user_view.logout_request, name= 'logout'),
    path('register/', user_view.register_request, name ='register'),
    path('dictionary/', website_view.dictionary, name='dictionary'),
    path('search/', website_view.search, name='search'),
    path('character_search', website_view.character_search, name='search'),
    path('chat/', chatbot_view.chatbot, name = 'chatbot'),
    path('save_quiz_scores/', user_view.save_quiz_scores, name='save_quiz_scores'),
    path('quiz_history/', user_view.quiz_history, name='quiz_history'),
    path('quiz_history/<uuid:quiz_id>/', user_view.quiz_details, name='quiz_details'),
]
