from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Quiz(models.Model):

    title = models.CharField(max_length=255)


class Score(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, related_name='quiz_score')
    score = models.IntegerField(default=0)

class Question(models.Model):

    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, related_name='quiz_question')
    description = models.TextField(blank=True, null=True)
    correct_answer = models.TextField(blank=True, null=True)
    

class Choices(models.Model):

    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='question')
    choice1 = models.TextField(blank=True, null=True)
    choice2 = models.TextField(blank=True, null=True)
    choice3 = models.TextField(blank=True, null=True)
    choice4 = models.TextField(blank=True, null=True)


class SubmitAnswer(models.Model):

    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='answer')
    answer = models.TextField(blank=True, null=True)
