from  rest_framework import serializers

from quiz.models import Question, SubmitAnswer, Choices, Score, Quiz


class ChoicesSerialzer(serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Choices


class QuestionSerializer(serializers.ModelSerializer):
    
    choices = serializers.SerializerMethodField()
    class Meta:
        fields = ['quiz', 'description', 'correct_answer', 'choices']
        model = Question

    def get_choices(self, obj):
        print("-------------")
        print(obj)
        try:
            choices = Choices.objects.get(question=obj)
            print(choices)
        except Choices.DoesNotExist:
            pass
        return ChoicesSerialzer(choices).data

class SubmitAnswerSerializer(serializers.Serializer):
    
    question_id = serializers.IntegerField()
    answer = serializers.CharField()

    def create(self, validated_data):
        print("----------------------")
        print(validated_data)
        print("----------------------")
        try:
            question = Question.objects.get(id=validated_data.get('question_id'))
            print(question)
        except Question.DoesNotExist:
            pass
        submit_answer = SubmitAnswer.objects.create(question=question, answer=validated_data.get('answer'))
        print("Created-----------------")
        return submit_answer


class ScoreSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Score




