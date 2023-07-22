from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Students
from .serializers import StudentSerializer
# Create your views here.


class StudentView(APIView):
     def get(self, request, *args, **kwargs):  
        result = Students.objects.all()  
        serializers = StudentSerializer(result, many=True)  
        return Response({'status': 'success', "students":serializers.data}, status=200)  
    