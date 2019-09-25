from django.urls import path
from app.api import views

urlpatterns = [
    path('users/', views.UserView.as_view()),
    path('users/<int:id>', views.UserView.as_view()),
    path('foods/', views.FoodView.as_view()),
    path('foods/<int:id>', views.FoodView.as_view()),
    path('recipes/', views.RecipeView.as_view()),
    path('recipes/<int:id>', views.RecipeView.as_view()),
    path('recipe_foods/', views.RecipeFoodView.as_view()),
    path('recipe_foods/<int:id>', views.RecipeFoodView.as_view()),
    path('favorites/', views.FavoriteView.as_view()),
    path('favorites/<int:id>', views.FavoriteView.as_view()),
    path('categories/', views.CategoryView.as_view()),
    path('categories/<int:id>', views.CategoryView.as_view()),
]
