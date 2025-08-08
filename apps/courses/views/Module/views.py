from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from apps.courses.models import Module
from apps.courses.serializers.Module.serializers import *

class ModuleListView(APIView):
    permission_classes = []
    def get(self, request):
        modules = Module.objects.all()
        serializer = ModuleListSerializer(modules, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ModuleDetailView(APIView):
    permission_classes = []
    def get(self, request, pk):
        try:
            module = Module.objects.get(pk=pk)
            serializer = ModuleDetailSerializer(module)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Module.DoesNotExist:
            return Response({"detail": "Module not found."}, status=status.HTTP_404_NOT_FOUND)
        
class ModuleCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ModuleCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ModuleUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request, pk):
        try:
            module = Module.objects.get(pk=pk)
            serializer = ModuleUpdateSerializer(module, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Module.DoesNotExist:
            return Response({"detail": "Module not found."}, status=status.HTTP_404_NOT_FOUND)
        
class ModuleDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        try:
            module = Module.objects.get(pk=pk)
            module.delete()
            return Response({"detail": "Module deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Module.DoesNotExist:
            return Response({"detail": "Module not found."}, status=status.HTTP_404_NOT_FOUND)