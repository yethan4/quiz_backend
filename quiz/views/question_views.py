from django.shortcuts import get_object_or_404
from rest_framework import generics

from quiz.models import Question, Quiz
from quiz.serializers import QuestionSerializer, QuestionsWithAnswersSerializer

class QuestionListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    
    def get_queryset(self):
        quiz_id = self.kwargs['quiz_id']
        return Question.objects.filter(quiz_id=quiz_id)

    def perform_create(self, serializer):
        quiz_id = self.kwargs['quiz_id']
        serializer.save(quiz_id=quiz_id)
        
class QuestionDestroyAPIView(generics.DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
class QuestionsWithAnswersCreateAPIView(generics.CreateAPIView):
    serializer_class = QuestionsWithAnswersSerializer

    def get_serializer_context(self):
        quiz_id = self.kwargs['quiz_id']
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        return {'quiz': quiz}
