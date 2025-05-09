from rest_framework import generics

from quiz.models import Answer
from quiz.serializers import AnswerSerializer


class AnswerListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    
    def get_queryset(self):
        question_id = self.kwargs['question_id']
        return Answer.objects.filter(question_id=question_id)
    
    def perform_create(self, serializer):
        question_id = self.kwargs['question_id']
        serializer.save(question_id=question_id)        
        
        
class AnswerDestroyAPIView(generics.DestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer