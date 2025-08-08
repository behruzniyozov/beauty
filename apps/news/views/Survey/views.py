from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.news.serializers.Survey.serializers import *
from apps.news.models import Survey


class SurveyListView(APIView):
    def get(self, request):
        surveys = Survey.objects.all()
        serializer = SurveyListSerializer(surveys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class SurveyDetailView(APIView):
    def get(self, request, pk):
        try:
            survey = Survey.objects.get(pk=pk)
            serializer = SurveyDetailSerializer(survey)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Survey.DoesNotExist:
            return Response({"error": "Survey not found"}, status=status.HTTP_404_NOT_FOUND)
        
class SurveyCreateView(APIView):
    def post(self, request):
        serializer = SurveyCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SurveyUpdateView(APIView):
    def put(self, request, pk):
        try:
            survey = Survey.objects.get(pk=pk)
            serializer = SurveyUpdateSerializer(survey, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Survey.DoesNotExist:
            return Response({"error": "Survey not found"}, status=status.HTTP_404_NOT_FOUND)
        
class SurveyDeleteView(APIView):
    def delete(self, request, pk):
        try:
            survey = Survey.objects.get(pk=pk)
            survey.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Survey.DoesNotExist:
            return Response({"error": "Survey not found"}, status=status.HTTP_404_NOT_FOUND)
        