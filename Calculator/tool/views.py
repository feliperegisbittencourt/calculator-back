from django.shortcuts import render
from rest_framework import generics, renderers, viewsets, status, permissions
from rest_framework.response import Response

from .models import *
from .serializers import *
from .functions import *

class Data_requestView(generics.ListAPIView):
    serializer_class = CalculatorSerializer
    queryset = Calculator.objects.all()
    
    def get(self, request, *args, **kwargs):
        resultado = self.request.data
        try:
            return Response( resultado, status=200)
        except:
            return Response("ERRO", status=500)

class ReportView(generics.ListCreateAPIView):
    serializer_class = CalculatorSerializer
    queryset = Calculator.objects.all()

    def get(self, request, *args, **kwargs):
        resultado = self.request.data
        return Response({"result": resultado})

    def post(self, request, *args, **kwargs):

        try:
            tag_pi = self.request.data
        except:
            return Response("Campo 'tag_pi' vazio", status=500)