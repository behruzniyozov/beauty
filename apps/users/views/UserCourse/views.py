from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from apps.users.serializers.UserCourse.serializers import *
from apps.users.models import UserCourse

class UserCourseListView(APIView):
    permission_classes = []

    def get(self, request):
        user_courses = UserCourse.objects.filter(user=request.user)
        serializer = UserCourseListSerializer(user_courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserCourseDetailView(APIView):
    permission_classes = []

    def get(self, request, pk):
        try:
            user_course = UserCourse.objects.get(pk=pk, user=request.user)
            serializer = UserCourseDetailSerializer(user_course)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserCourse.DoesNotExist:
            return Response({"error": "User course not found"}, status=status.HTTP_404_NOT_FOUND)
        
class UserCourseCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = UserCourseCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserCourseUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        try:
            user_course = UserCourse.objects.get(pk=pk, user=request.user)
            serializer = UserCourseUpdateSerializer(user_course, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except UserCourse.DoesNotExist:
            return Response({"error": "User course not found"}, status=status.HTTP_404_NOT_FOUND)
        
class UserCourseDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        try:
            user_course = UserCourse.objects.get(pk=pk, user=request.user)
            user_course.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except UserCourse.DoesNotExist:
            return Response({"error": "User course not found"}, status=status.HTTP_404_NOT_FOUND)
        