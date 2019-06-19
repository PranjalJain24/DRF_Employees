from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employees
from .serializers import employeeSerializer

## request api and get json back

class employeeList(APIView):
    def get(self, request):
        employees1 = employees.objects.all()
        serializer = employeeSerializer(employees1, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass