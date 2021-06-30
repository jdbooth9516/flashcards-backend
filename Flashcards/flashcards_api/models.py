from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    total_cards = models.IntegerField(default=0)

class Cards(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.CharField(max_length=100, blank=False)
    answer = models.CharField(max_length=200, blank=False)