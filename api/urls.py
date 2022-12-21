from django.urls import path
from .views import QuizListView, QuestionListView, TopicListView, CheckAnswerView, GetResultView

urlpatterns = [
    path('quiz/', QuizListView.as_view()),
    path('question/', QuestionListView.as_view()),
    path('topic/', TopicListView.as_view()),
    path('check/', CheckAnswerView.as_view()),
    path('result/', GetResultView.as_view())
]
