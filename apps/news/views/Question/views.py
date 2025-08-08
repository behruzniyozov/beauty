from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.news.serializers.Question.serializers import *
from apps.news.models import Question

class QuestionListView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionListSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class QuestionDetailView(APIView):
    def get(self, request, pk):
        try:
            question = Question.objects.get(pk=pk)
            serializer = QuestionDetailSerializer(question)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Question.DoesNotExist:
            return Response({"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND)
        
class QuestionCreateView(APIView):
    def post(self, request):
        serializer = QuestionCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class QuestionUpdateView(APIView):
    def put(self, request, pk):
        try:
            question = Question.objects.get(pk=pk)
            serializer = QuestionUpdateSerializer(question, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Question.DoesNotExist:
            return Response({"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND)
        

class QuestionDeleteView(APIView):
    def delete(self, request, pk):
        try:
            question = Question.objects.get(pk=pk)
            question.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Question.DoesNotExist:
            return Response({"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND)