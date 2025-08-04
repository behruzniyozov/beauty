from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from beauty.apps.courses.models import Webinar
from beauty.apps.courses.serializers.Webinar.serializers import *

class WebinarListView(APIView):
    def get(self, request):
        webinars = Webinar.objects.all()
        serializer = WebinarListSerializer(webinars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class WebinarDetailView(APIView):
    def get(self, request, pk):
        try:
            webinar = Webinar.objects.get(pk=pk)
            serializer = WebinarDetailSerializer(webinar)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Webinar.DoesNotExist:
            return Response({"detail": "Webinar not found."}, status=status.HTTP_404_NOT_FOUND)
        
class WebinarCreateView(APIView):
    def post(self, request):
        serializer = WebinarCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class WebinarUpdateView(APIView):
    def put(self, request, pk):
        try:
            webinar = Webinar.objects.get(pk=pk)
            serializer = WebinarUpdateSerializer(webinar, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Webinar.DoesNotExist:
            return Response({"detail": "Webinar not found."}, status=status.HTTP_404_NOT_FOUND)
        
class WebinarDeleteView(APIView):
    def delete(self, request, pk):
        try:
            webinar = Webinar.objects.get(pk=pk)
            webinar.delete()
            return Response({"detail": "Webinar deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Webinar.DoesNotExist:
            return Response({"detail": "Webinar not found."}, status=status.HTTP_404_NOT_FOUND)