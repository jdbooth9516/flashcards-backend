from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
    path('cards/', views.CardsList.as_view()),
    path('cards_category/<int:category_id>', views.CardsByCategory.as_view()),
    path('cards_category/<int:category_id>/<int:pk>/',views.CardDetails.as_view()),

]