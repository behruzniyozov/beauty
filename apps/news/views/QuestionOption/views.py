from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.news.serializers.QuestionOption.serializers import *
from apps.news.models import QuestionOption

class QuestionOptionListView(APIView):
    def get(self, request):
        options = QuestionOption.objects.all()
        serializer = QuestionOptionListSerializer(options, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class QuestionOptionDetailView(APIView):
    def get(self, request, pk):
        try:
            option = QuestionOption.objects.get(pk=pk)
            serializer = QuestionOptionDetailSerializer(option)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except QuestionOption.DoesNotExist:
            return Response({"error": "Question Option not found"}, status=status.HTTP_404_NOT_FOUND)
        
class QuestionOptionCreateView(APIView):
    def post(self, request):
        serializer = QuestionOptionCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class QuestionOptionUpdateView(APIView):
    def put(self, request, pk):
        try:
            option = QuestionOption.objects.get(pk=pk)
            serializer = QuestionOptionUpdateSerializer(option, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except QuestionOption.DoesNotExist:
            return Response({"error": "Question Option not found"}, status=status.HTTP_404_NOT_FOUND)
        
class QuestionOptionDeleteView(APIView):
    def delete(self, request, pk):
        try:
            option = QuestionOption.objects.get(pk=pk)
            option.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except QuestionOption.DoesNotExist:
            return Response({"error": "Question Option not found"}, status=status.HTTP_404_NOT_FOUND)