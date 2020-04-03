from rest_framework import serializers
from .models import *

class CalculatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calculator
        fields = '__all__'