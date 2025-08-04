from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from beauty.apps.courses.models import Lesson
from beauty.apps.courses.serializers.Lesson.serializers import *

class LessonListView(APIView):
    def get(self, request):
        lessons = Lesson.objects.all()
        serializer = LessonListSerializer(lessons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class LessonDetailView(APIView):
    def get(self, request, pk):
        try:
            lesson = Lesson.objects.get(pk=pk)
            serializer = LessonDetailSerializer(lesson)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Lesson.DoesNotExist:
            return Response({"detail": "Lesson not found."}, status=status.HTTP_404_NOT_FOUND)
        
class LessonCreateView(APIView):
    def post(self, request):
        serializer = LessonCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LessonUpdateView(APIView):
    def put(self, request, pk):
        try:
            lesson = Lesson.objects.get(pk=pk)
            serializer = LessonUpdateSerializer(lesson, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Lesson.DoesNotExist:
            return Response({"detail": "Lesson not found."}, status=status.HTTP_404_NOT_FOUND)
        

class LessonDeleteView(APIView):
    def delete(self, request, pk):
        try:
            lesson = Lesson.objects.get(pk=pk)
            lesson.delete()
            return Response({"detail": "Lesson deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Lesson.DoesNotExist:
            return Response({"detail": "Lesson not found."}, status=status.HTTP_404_NOT_FOUND)