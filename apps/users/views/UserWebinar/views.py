from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from apps.users.serializers.UserWebinar.serializers import *
from apps.users.models import UserWebinar

class UserWebinarListView(APIView):
    permission_classes = []

    def get(self, request):
        user_webinars = UserWebinar.objects.filter(user=request.user)
        serializer = UserWebinarListSerializer(user_webinars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserWebinarDetailView(APIView):
    permission_classes = []

    def get(self, request, pk):
        try:
            user_webinar = UserWebinar.objects.get(pk=pk, user=request.user)
            serializer = UserWebinarDetailSerializer(user_webinar)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserWebinar.DoesNotExist:
            return Response({"error": "User webinar not found"}, status=status.HTTP_404_NOT_FOUND)
        
class UserWebinarCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = UserWebinarCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserWebinarUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        try:
            user_webinar = UserWebinar.objects.get(pk=pk, user=request.user)
            serializer = UserWebinarUpdateSerializer(user_webinar, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except UserWebinar.DoesNotExist:
            return Response({"error": "User webinar not found"}, status=status.HTTP_404_NOT_FOUND)

class UserWebinarDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        try:
            user_webinar = UserWebinar.objects.get(pk=pk, user=request.user)
            user_webinar.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except UserWebinar.DoesNotExist:
            return Response({"error": "User webinar not found"}, status=status.HTTP_404_NOT_FOUND)
        