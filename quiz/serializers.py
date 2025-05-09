from wsgiref import validate
from rest_framework import serializers
from .models import Quiz, Question, Answer, UserQuizResult

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text', 'is_correct']
    
class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'text', 'answers']
        
class SingleQuestionWithAnswersSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    
    class Meta:
        model = Question
        fields = ['text', 'answers']
        
    def create(self, validated_data):
        answers_data = validated_data.pop('answers')
        quiz = self.context['quiz']
        question = Question.objects.create(quiz=quiz, **validated_data)
        for answer_data in answers_data:
            Answer.objects.create(question=question, **answer_data)
        return question
    
class QuestionsWithAnswersSerializer(serializers.Serializer):
    questions = SingleQuestionWithAnswersSerializer(many=True)
    
    def create(self, validated_data):
        quiz = self.context['quiz']
        questions_data = validated_data['questions']
        created_questions = []
        for question_data in questions_data:
            serializer = SingleQuestionWithAnswersSerializer(data=question_data, context={'quiz': quiz})
            serializer.is_valid(raise_exception=True)
            created_questions.append(serializer.save())
        return {'questions': created_questions}
        
class QuizSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description']
        
class QuizDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description']
        
class UserQuizResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuizResult
        fields = ['id', 'user', 'quiz', 'score', 'completed_at']