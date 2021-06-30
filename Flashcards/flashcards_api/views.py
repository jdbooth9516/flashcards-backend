from .models import Category, Cards
from .serializers import CategorySerializer, CardsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class CategoryList(APIView): 

    def get(self, request): 
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
