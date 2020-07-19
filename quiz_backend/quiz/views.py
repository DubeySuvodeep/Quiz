from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.views import status

from django.contrib.auth.models import User
from quiz.models import Question, SubmitAnswer, Choices, Quiz, Score
from quiz.serializer import QuestionSerializer, SubmitAnswerSerializer, ChoicesSerialzer, ScoreSerializer



class Questions(APIView):
    
    def get(self, request):
        if request.user.is_authenticated:
            try:
                questions = Question.objects.all()
                serializer = QuestionSerializer(questions, many=True)
                
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={"detail": "Invalid username/password."})


class QuestionDetail(APIView):
    
    def get(self, request, question_id):
        if request.user.is_authenticated:
            try:
                questions = Question.objects.get(id=question_id)
                serializer = QuestionSerializer(questions)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            except Question.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={"detail": "Invalid username/password."})

class SubmitAnswer(APIView):
    
    def post(self, request, **kwargs):
        if request.user.is_authenticated:
            serializer = SubmitAnswerSerializer(data=request.data)
            if serializer.is_valid():
                
                s = serializer.save()
                print(s)
                score = Score.objects.get(quiz=s.question.quiz)
                print("Initial score")
                print(score.score)
                if s.question.correct_answer == s.answer:
                    score.score += 2
                    score.save()
                print("New score")
                print(score.score)

                return Response(status=status.HTTP_200_OK)
            else:
                print(serializer.errors)
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={"detail": "Invalid username/password."})


class AssessmentReport(APIView):
    
    def get(self, request):
        if request.user.is_authenticated:
            try:
                quiz = Quiz.objects.get(id=request.data.get('quiz_id'))
                user = User.objects.get(id=request.data.get('user_id'))
                score = Score.objects.get(user=user, quiz=quiz)
                serializer = ScoreSerializer(score)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            except Quiz.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={"detail": "Invalid username/password."})