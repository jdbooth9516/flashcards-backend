from rest_framework.serializers import Serializer
from .models import Category, Cards
from .serializers import CategorySerializer, CardsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class CategoryList(APIView): 
    # grabing a list of the all the categories
    def get(self, request): 
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    # adding a category to the DB
    def post(self, request): 
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
class CategoryDetail(APIView):        

    def get_category(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        category = self.get_category(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
        
    
    def put(self, request, pk):
        category = self.get_category(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CardsList(APIView):

    def get(self, request): 
        categories = Cards.objects.all()
        serializer = CardsSerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CardsSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class CardsByCategory(APIView):

    def get_cards(self, category_id):
        try:
            return Cards.objects.filter(category_id=category_id)
        except Cards.DoesNotExist:
            raise Http404

    def get(self, request, category_id):
        cards = self.get_cards(category_id)
        serializer = CardsSerializer(cards, many=True)
        return Response(serializer.data)


class CardDetails(APIView):

    def get_card(self, pk):
        try:
            return Cards.objects.get(pk=pk)
        except Cards.DoesNotExist:
            raise Http404

    def get(self, request, category_id, pk):
        card = self.get_card(pk)
        serializer = CardsSerializer(card)
        return Response(serializer.data)

    def put(self, request, category_id, pk):
        card = self.get_card(pk)