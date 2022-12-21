from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status



from .serializers import QuizSerializer, QuestionSerializer, OptionSerializer, TopicSerializer, StudentSerializer, ResultSerializer, ResultDetailSerializer
# Create your views here.

from .models import Quiz, Question, Option, Student, Result, ResultDetail, Topic


# View for get all quiz
class QuizListView(APIView):
    
    def post(self, request:Request):
        data = request.data
        serializer = QuizSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def get(self, request: Request):
        quiz = Quiz.objects.all()
        serializer = QuizSerializer(quiz, many=True)
        return Response(serializer.data)

class QuestionListView(APIView):
    
    def post(self, request:Request):
        data = request.data
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def get(self, request:Request, pk):
        
        topic_filter = Topic.objects.filter(id=pk)
        topic = TopicSerializer(topic_filter, many = False)
        
        quiz_filter = Quiz.objects.filter(id = topic.data['quiz'])
        quiz = QuizSerializer(quiz_filter, many = False)
        
        question_filter = Question.objects.filter(quiz = pk)
        question = QuestionSerializer(question_filter, many = True)
        

class TopicListView(APIView):
    
    def post(self, request:Request):
        data = request.data
        serializer = TopicSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def get(self, request:Request, pk):
        
        topic_filter = Topic.objects.filter(quiz=pk)
        topic = TopicSerializer(topic_filter, many = True)
        
        quiz_filter = Quiz.objects.filter(quiz = pk)
        quiz = QuestionSerializer(quiz_filter, many = False)
        data = {
            'quiz':{
                'id':quiz.data['id'],
                'title':quiz.data['title'],
                'description':quiz.data['description'],
                'topics':topic.data
            }
        }    
        
        return Response(data)

class CheckAnswerView(APIView):
    
    def get(self, request:Request):
        
        pass

class GetResultView(APIView):
    
    def get(self, request:Request):
        
        pass