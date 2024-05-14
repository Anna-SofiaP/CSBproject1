import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    answer_date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s answer to {self.question.question_text}: {self.choice_text}"

    
#votes = models.IntegerField(default=0)

