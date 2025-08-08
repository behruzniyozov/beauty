from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.news.serializers.Submission.serializers import *
from apps.news.models import Submission

class SubmissionListView(APIView):
    def get(self, request):
        submissions = Submission.objects.all()
        serializer = SubmissionListSerializer(submissions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class SubmissionDetailView(APIView):
    def get(self, request, pk):
        try:
            submission = Submission.objects.get(pk=pk)
            serializer = SubmissionDetailSerializer(submission)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Submission.DoesNotExist:
            return Response({"error": "Submission not found"}, status=status.HTTP_404_NOT_FOUND)
        
class SubmissionCreateView(APIView):
    def post(self, request):
        serializer = SubmissionCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SubmissionUpdateView(APIView):
    def put(self, request, pk):
        try:
            submission = Submission.objects.get(pk=pk)
            serializer = SubmissionUpdateSerializer(submission, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Submission.DoesNotExist:
            return Response({"error": "Submission not found"}, status=status.HTTP_404_NOT_FOUND)
        
class SubmissionDeleteView(APIView):
    def delete(self, request, pk):
        try:
            submission = Submission.objects.get(pk=pk)
            submission.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Submission.DoesNotExist:
            return Response({"error": "Submission not found"}, status=status.HTTP_404_NOT_FOUND)
        