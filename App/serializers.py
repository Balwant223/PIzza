from rest_framework import serializers
from .models import Pizza

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pizza
        fields=['id','Type','Size','Topping']