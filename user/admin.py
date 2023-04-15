from django.contrib import admin
from .models import QuizScore
from django.utils.html import mark_safe

class QuizScoreAdmin(admin.ModelAdmin):
    #list_display = ('id', 'user', 'quiz_name', 'score', 'total_questions', 'timestamp', 'display_words')
    list_display = ('id', 'user', 'quiz_name', 'score', 'total_questions', 'timestamp')

    def display_words(self, obj):
        return mark_safe('<br>'.join(obj.words))
    display_words.short_description = 'Words'


# Register your models here.
admin.site.register(QuizScore, QuizScoreAdmin)

