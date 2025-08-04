from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from beauty.apps.courses.models import Course
from beauty.apps.courses.serializers.Course.serializers import *

class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseListSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CourseDetailView(APIView):
    def get(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
            serializer = CourseDetailSerializer(course)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response({"detail": "Course not found."}, status=status.HTTP_404_NOT_FOUND)
        
class CourseCreateView(APIView):
    def post(self, request):
        serializer = CourseCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CourseUpdateView(APIView):
    def put(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
            serializer = CourseUpdateSerializer(course, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Course.DoesNotExist:
            return Response({"detail": "Course not found."}, status=status.HTTP_404_NOT_FOUND)
        
class CourseDeleteView(APIView):
    def delete(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
            course.delete()
            return Response({"detail": "Course deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Course.DoesNotExist:
            return Response({"detail": "Course not found."}, status=status.HTTP_404_NOT_FOUND)