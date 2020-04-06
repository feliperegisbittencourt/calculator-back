from django.shortcuts import render
from rest_framework import generics, renderers, viewsets, status, permissions
from rest_framework.response import Response

from .models import *
from .serializers import *

#class API
class ReportView(generics.ListCreateAPIView):
    #serializer import
    serializer_class = CalculatorSerializer
    #get all Calculator Model's fields
    queryset = Calculator.objects.all()

    #create post function
    def post(self, request, *args, **kwargs):
        api_data = 0
        #get api body data
        api_data = self.request.data
        
        #get field numbers of api body
        numbers = api_data['numbers']
        #get field operators of api body
        operators = api_data['operators']
        
        index = 0
        finalResult = 0
        #go through the array
        while index < (len(numbers)):
            #check if has operator * in array operators
            if '*' in operators:
                #get the *'s index
                indexm = operators.index("*")
                #check if has operator / in array operators
                if '/' in operators:
                    #get the /'s index
                    indexd = operators.index("/")
                    #compare index of multiply and divide to do first that first write
                    if indexm < indexd:
                        #get the *'s index
                        indexm = operators.index("*")
                        #validate if last item on view, isn't a operator
                        if indexm + 1 > len(numbers):
                            numbers[indexm + 1] = 0
                        #validate if last item on view, isn't a operator
                        if indexd +1 > len(numbers):
                            numbers[indexd + 1] = 0
                        #do the multiply operation
                        result = float(numbers[indexm]) * float(numbers[indexm + 1])
                        #del the second number of operation
                        del numbers[indexm + 1]
                        #set the result in first number of operation place
                        numbers[indexm] = result
                        #del the operator
                        del operators[indexm]
                        #get the /'s index
                        indexd = operators.index("/")
                        #validade if was a division per zero
                        if numbers[indexd + 1] == '0':
                            result = 0
                        else:
                            result = float(numbers[indexd]) / float(numbers[indexd + 1])
                        #del the second number of operation
                        del numbers[indexd+1]
                        #set the result in first number of operation place
                        numbers[indexd] = result
                        #del the operator
                        del operators[indexd]
                        #go to intial of array
                        indexd = index
                        indexm = index
                    else:
                        #get the /'s index
                        indexd = operators.index("/")
                        #validade if was a division per zero
                        if numbers[indexd + 1] == '0':
                            result = 0
                        else:
                            result = float(numbers[indexd]) / float(numbers[indexd + 1])
                        #del the second number of operation
                        del numbers[indexd+1]
                        #set the result in first number of operation place
                        numbers[indexd] = result
                        #del the operator
                        del operators[indexd]
                        indexm = operators.index("*")
                        result = float(numbers[indexm]) * float(numbers[indexm + 1])
                        #del the second number of operation
                        del numbers[indexm + 1]
                        #set the result in first number of operation place
                        numbers[indexm] = result
                        #del the operator
                        del operators[indexm]
                        index = 0
                        #go to intial of array
                        indexd = index
                        indexm = index
                else:
                    #get the *'s index
                    indexm = operators.index("*")
                    result = float(numbers[indexm]) * float(numbers[indexm + 1])
                    #del the second number of operation
                    del numbers[indexm + 1]
                    #set the result in first number of operation place
                    numbers[indexm] = result
                    #del the operator
                    del operators[indexm]
                    #go to intial of array
                    index = 0
                    indexm = index
            #check if has operator / in array operators and no has operator *
            elif '/' in operators:
                #get the /'s index
                indexd = operators.index("/")

                #validate if last item on view, isn't a operator
                if indexd +1 > len(numbers):
                    numbers[indexd + 1] = 0
                #validade if was a division per zero
                if numbers[indexd + 1] == '0':
                    result = 0
                else:
                    result = float(numbers[indexd]) / float(numbers[indexd + 1])
                #del the second number of operation
                del numbers[indexd+1]
                #set the result in first number of operation place
                numbers[indexd] = result
                #del the operator
                del operators[indexd]
                #go to intial of array
                index = 0
                indexd = index
            #check if has operator + in array operators
            if '+' in operators:
                #get the +'s index
                indexp = operators.index("+")
                #check if has operator - in array operators
                if '-' in operators:
                    #get the -'s index
                    indexs = operators.index("-")
                    #compare index of addition and subtration to do first that first write
                    if indexp < indexs:
                        #get the +'s index
                        indexp = operators.index("+")
                        result = float(numbers[indexp]) + float(numbers[indexp + 1])
                        #del the second number of operation
                        del numbers[indexp + 1]
                        #set the result in first number of operation place
                        numbers[indexp] = result
                        #del the operator
                        del operators[indexp]
                        #get the -'s index
                        indexs = operators.index("-")
                        result = float(numbers[indexs]) - float(numbers[indexs + 1])
                        #del the second number of operation
                        del numbers[indexs+1]
                        #set the result in first number of operation place
                        numbers[indexs] = result
                        #del the operator
                        del operators[indexs]
                        #go to intial of array
                        index = 0
                        indexp = index
                        indexs = index
                    else:
                        #get the -'s index
                        indexs = operators.index("-")
                        result = float(numbers[indexs]) - float(numbers[indexs + 1])
                        #del the second number of operation
                        del numbers[indexs + 1]
                        #set the result in first number of operation place
                        numbers[indexs] = result
                        #del the operator
                        del operators[indexs]
                        #get the +'s index
                        indexp = operators.index("+")
                        result = float(numbers[indexp]) + float(numbers[indexp + 1])
                        #del the second number of operation
                        del numbers[indexp+1]
                        #set the result in first number of operation place
                        numbers[indexp] = result
                        #del the operator
                        del operators[indexp]
                        #go to intial of array
                        index = 0
                        indexp = index
                        indexs = index
                else:
                    #get the +'s index
                    indexp = operators.index("+")
                    result = float(numbers[indexp]) + float(numbers[indexp + 1])
                    #del the second number of operation
                    del numbers[indexp + 1]
                    #set the result in first number of operation place
                    numbers[indexp] = result
                    #del the operator
                    del operators[indexp]
                    #go to intial of array
                    index = 0
                    indexp = index
            #check if has operator - in array operators
            if '-' in operators:
                #get the -'s index
                indexs = operators.index("-")
                result = float(numbers[indexs]) - float(numbers[indexs + 1])
                #del the second number of operation
                del numbers[indexs + 1]
                #set the result in first number of operation place
                numbers[indexs] = result
                #del the operator
                del operators[indexs]
                #go to intial of array
                index = 0
                indexs = index
                                
            
            #set finalResult that the first number of numbers
            finalResult = numbers[0]
            #update index
            index += 1
        #return the final result
        return Response({"result": finalResult})
        #try:
        #    tag_pi = self.request.data
        #except:
        #    return Response("Campo 'tag_pi' vazio", status=500)