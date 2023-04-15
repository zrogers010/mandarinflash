from django.db import models
from django.contrib.auth.models import User
import uuid

class QuizScore(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz_name = models.CharField(max_length=255)
    score = models.IntegerField()
    total_questions = models.IntegerField()
    words = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz_name} - {self.score}/{self.total_questions}"
