from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from apps.users.serializers.Interest.serializers import *
from apps.users.models import Interest

class InterestListView(APIView):
    permission_classes = []

    def get(self, request):
        interests = Interest.objects.filter(user=request.user)
        serializer = InterestListSerializer(interests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    

class InterestDetailView(APIView):
    permission_classes = []

    def get(self, request, pk):
        try:
            interest = Interest.objects.get(pk=pk, user=request.user)
            serializer = InterestDetailSerializer(interest)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Interest.DoesNotExist:
            return Response({"error": "Interest not found"}, status=status.HTTP_404_NOT_FOUND)
        
class InterestCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = InterestCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class InterestUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        try:
            interest = Interest.objects.get(pk=pk, user=request.user)
            serializer = InterestUpdateSerializer(interest, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Interest.DoesNotExist:
            return Response({"error": "Interest not found"}, status=status.HTTP_404_NOT_FOUND)
        

class InterestDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        try:
            interest = Interest.objects.get(pk=pk, user=request.user)
            interest.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Interest.DoesNotExist:
            return Response({"error": "Interest not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)