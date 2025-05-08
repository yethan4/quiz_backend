from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    AnswerDestroyAPIView,
    QuestionDestroyAPIView,
    QuizDestroyAPIView,
    QuizListCreateAPIView,
    QuizDetailAPIView,
    QuestionListCreateAPIView,
    AnswerListCreateAPIView
)


urlpatterns = [
    path('quizzes/', QuizListCreateAPIView.as_view(), name='quiz-list-create'),
    path('quizzes/<int:pk>/', QuizDetailAPIView.as_view(), name='quiz-detail'),
    path('quizzes/<int:quiz_id>/questions/', QuestionListCreateAPIView.as_view(), name='question-list-create'),
    path('questions/<int:question_id>/answers/', AnswerListCreateAPIView.as_view(), name='answer-list-create'),
    
    path('quizzes/<int:pk>/delete/', QuizDestroyAPIView.as_view(), name='quiz-delete'),
    path('questions/<int:pk>/delete/', QuestionDestroyAPIView.as_view(), name='question-delete'),
    path('answers/<int:pk>/delete/', AnswerDestroyAPIView.as_view(), name='answer-delete'),
]
