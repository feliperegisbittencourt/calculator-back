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
        resultad = self.request.data
        """ numbers = resultad['numbers']
        operators = resultad['operators']
        index = 0
        while index < (len(numbers)-1):
            if '*' in operators:
                indexm = operators.index("*")
                if '/' in operators:
                    indexd = operators.index("/")
                    if indexm < indexd:
                        indexm = operators.index("*")
                        result = numbers[indexm] * numbers[indexm + 1]
                        del numbers[indexm + 1]
                        numbers[indexm] = result
                        del operators[indexm]
                        indexd = operators.index("/")
                        result = numbers[indexd] / numbers[indexd + 1]
                        del numbers[indexd+1]
                        numbers[indexd] = result
                        del operators[indexd]
                    else:
                        indexd = operators.index("/")
                        result = numbers[indexd] / numbers[indexd + 1]
                        del numbers[indexd+1]
                        numbers[indexd] = result
                        del operators[indexd]
                        indexm = operators.index("*")
                        result = numbers[indexm] * numbers[indexm + 1]
                        del numbers[indexm + 1]
                        numbers[indexm] = result
                        del operators[indexm]
                else:
                    indexm = operators.index("*")
                    result = numbers[indexm] * numbers[indexm + 1]
                    del numbers[indexm + 1]
                    numbers[indexm] = result
                    del operators[indexm]
            elif '/' in operators:
                indexd = operators.index("/")
                result = numbers[indexd] / numbers[indexd + 1]
                del numbers[indexd+1]
                numbers[indexd] = result
                del operators[indexd]
            if '+' in operators:
                indexp = operators.index("+")
                if '-' in operators:
                    indexs = operators.index("-")
                    if indexp < indexs:
                        indexp = operators.index("+")
                        result = numbers[indexp] + numbers[indexp + 1]
                        del numbers[indexp + 1]
                        numbers[indexp] = result
                        del operators[indexp]
                        indexs = operators.index("-")
                        result = numbers[indexs] - numbers[indexs + 1]
                        del numbers[indexs+1]
                        numbers[indexs] = result
                        del operators[indexs]
                    else:
                        indexs = operators.index("-")
                        result = numbers[indexs] - numbers[indexs + 1]
                        del numbers[indexs + 1]
                        numbers[indexs] = result
                        del operators[indexs]
                        indexp = operators.index("+")
                        result = numbers[indexp] + numbers[indexp + 1]
                        del numbers[indexp+1]
                        numbers[indexp] = result
                        del operators[indexp]
                else:
                    indexp = operators.index("+")
                    result = numbers[indexp] + numbers[indexp + 1]
                    del numbers[indexp + 1]
                    numbers[indexp] = result
                    del operators[indexp]
            elif '-' in operators:
                indexs = operators.index("-")
                result = numbers[indexs] - numbers[indexs + 1]
                del numbers[indexs + 1]
                numbers[indexs] = result
                del operators[indexs]
                                
            
            
            resultado = numbers[0]
            index = len(numbers)
         """

        print(resultad)
        
        return Response({"result": resultad})

    def post(self, request, *args, **kwargs):
        resultad = 0
        resultad = self.request.data
        
        numbers = resultad['numbers']
        operators = resultad['operators']
        index = 0
        while index < (len(numbers)-1):
            if '*' in operators:
                indexm = operators.index("*")
                if '/' in operators:
                    indexd = operators.index("/")
                    if indexm < indexd:
                        indexm = operators.index("*")
                        result = int(numbers[indexm]) * int(numbers[indexm + 1])
                        del numbers[indexm + 1]
                        numbers[indexm] = result
                        del operators[indexm]
                        indexd = operators.index("/")
                        result = int(numbers[indexd]) / int(numbers[indexd + 1])
                        del numbers[indexd+1]
                        numbers[indexd] = result
                        del operators[indexd]
                    else:
                        indexd = operators.index("/")
                        result = numbers[indexd] / numbers[indexd + 1]
                        del numbers[indexd+1]
                        numbers[indexd] = result
                        del operators[indexd]
                        indexm = operators.index("*")
                        result = numbers[indexm] * numbers[indexm + 1]
                        del numbers[indexm + 1]
                        numbers[indexm] = result
                        del operators[indexm]
                else:
                    indexm = operators.index("*")
                    result = int(numbers[indexm]) * int(numbers[indexm + 1])
                    del numbers[indexm + 1]
                    numbers[indexm] = result
                    del operators[indexm]
            elif '/' in operators:
                indexd = operators.index("/")
                result = numbers[indexd] / numbers[indexd + 1]
                del numbers[indexd+1]
                numbers[indexd] = result
                del operators[indexd]
            if '+' in operators:
                indexp = operators.index("+")
                if '-' in operators:
                    indexs = operators.index("-")
                    if indexp < indexs:
                        indexp = operators.index("+")
                        result = numbers[indexp] + numbers[indexp + 1]
                        del numbers[indexp + 1]
                        numbers[indexp] = result
                        del operators[indexp]
                        indexs = operators.index("-")
                        result = numbers[indexs] - numbers[indexs + 1]
                        del numbers[indexs+1]
                        numbers[indexs] = result
                        del operators[indexs]
                    else:
                        indexs = operators.index("-")
                        result = numbers[indexs] - numbers[indexs + 1]
                        del numbers[indexs + 1]
                        numbers[indexs] = result
                        del operators[indexs]
                        indexp = operators.index("+")
                        result = numbers[indexp] + numbers[indexp + 1]
                        del numbers[indexp+1]
                        numbers[indexp] = result
                        del operators[indexp]
                else:
                    indexp = operators.index("+")
                    result = numbers[indexp] + numbers[indexp + 1]
                    del numbers[indexp + 1]
                    numbers[indexp] = result
                    del operators[indexp]
            elif '-' in operators:
                indexs = operators.index("-")
                result = numbers[indexs] - numbers[indexs + 1]
                del numbers[indexs + 1]
                numbers[indexs] = result
                del operators[indexs]
                                
            
            
            resultado = numbers[0]
            index = len(numbers)
        print(resultado)
        
        return Response({"result": resultado})
        #try:
        #    tag_pi = self.request.data
        #except:
        #    return Response("Campo 'tag_pi' vazio", status=500)