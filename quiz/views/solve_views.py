from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from quiz.models import Question

class SolveQuizAPIView(APIView):
    def post(self, request, quiz_id):
        selected_answer_ids = request.data.get('answers', [])
        
        questions = Question.objects.filter(quiz_id=quiz_id).prefetch_related('answers')
        total_questions = questions.count()
        
        if total_questions == 0:
            return Response({'detail': 'This quiz has no questions.'}, status=status.HTTP_400_BAD_REQUEST)
        
        correct_count = 0
        for question in questions:
            correct_answer = question.answers.filter(is_correct=True).first()
            if correct_answer and correct_answer.id in selected_answer_ids:
                correct_count += 1
        
        score_percent = round((correct_count / total_questions) * 100, 2)
        
        return Response({
            'correct': correct_count,
            'total': total_questions,
            'score_percent': score_percent
        })