from django.contrib import admin

from quiz.models import Question, SubmitAnswer, Choices, Score, Quiz
# Register your models here.

admin.site.register(Question)
admin.site.register(SubmitAnswer)
admin.site.register(Choices)
admin.site.register(Score)
admin.site.register(Quiz)
