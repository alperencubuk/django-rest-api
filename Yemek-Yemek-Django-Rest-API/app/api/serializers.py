from rest_framework import serializers
from app.api.models import User, Food, Recipe, RecipeFood, Favorite, Category


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password',
            'email'
        )


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = (
            'name',
            'image',
            'calorie',
            'carbohydrate',
            'protein',
            'fat',
            'health_point',
            'category',
            'description'
        )


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            'name',
            'image',
            'rating',
            'calorie',
            'carbohydrate',
            'protein',
            'fat',
            'cooking_minutes',
            'description'
        )


class RecipeFoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RecipeFood
        fields = ('recipe_id', 'food_id')


class FavoriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Favorite
        fields = ('user_id', 'recipe_id')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('category')