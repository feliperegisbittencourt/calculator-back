from rest_framework import serializers
from .models import *


#Serializer Calculator import model Calculator and all fields

class CalculatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calculator
        fields = '__all__'