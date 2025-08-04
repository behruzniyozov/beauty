from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from beauty.apps.courses.models import Comment
from beauty.apps.courses.serializers.Comment.serializers import *

class CommentListView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CommentDetailView(APIView):
    def get(self, request, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentDetailSerializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Comment.DoesNotExist:
            return Response({"detail": "Comment not found."}, status=status.HTTP_404_NOT_FOUND)
        
class CommentCreateView(APIView):
    def post(self, request):
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CommentUpdateView(APIView):
    def put(self, request, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentUpdateSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Comment.DoesNotExist:
            return Response({"detail": "Comment not found."}, status=status.HTTP_404_NOT_FOUND)
        
class CommentDeleteView(APIView):
    def delete(self, request, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            comment.delete()
            return Response({"detail": "Comment deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            return Response({"detail": "Comment not found."}, status=status.HTTP_404_NOT_FOUND)