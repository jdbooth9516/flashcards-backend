from rest_framework import serializers
from .models import Category, Cards


class CategorySerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Category
        fields = ['id','name', 'total_cards']

class CardsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Cards
        fields = ['id','category', 'question', 'answer']
        