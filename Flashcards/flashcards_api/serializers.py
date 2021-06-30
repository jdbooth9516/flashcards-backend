from rest_framework import serializers
from .models import Category, Cards


class CategorySerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Category
        fields = ['name', 'total_cards']

class CardsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Cards
        fields = ['category', 'question', 'answer']
        