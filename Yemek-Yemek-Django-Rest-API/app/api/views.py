from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from app.api.models import User, Food, Recipe, RecipeFood, Favorite, Category
from app.api.serializers import UserSerializer, FoodSerializer, RecipeSerializer, RecipeFoodSerializer, FavoriteSerializer, CategorySerializer


class UserView(APIView):
    def get(self, request, id=None, *args, **kwargs):
        if id:
            serializer = UserSerializer(User.objects.get(id=id))
        else:
            serializer = UserSerializer(User.objects.all(), many=True)
        return Response(serializer.data, status=200)

    
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class FoodView(APIView):
    def get(self, request, id=None, *args, **kwargs):
        if id:
            serializer = FoodSerializer(Food.objects.get(id=id))
        else:
            serializer = FoodSerializer(Food.objects.all(), many=True)
        return Response(serializer.data, status=200)


    def post(self, request, *args, **kwargs):
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class RecipeView(APIView):
    def get(self, request, id=None, *args, **kwargs):
        if id:
            serializer = RecipeSerializer(Recipe.objects.get(id=id))
        else:
            serializer = RecipeSerializer(Recipe.objects.all(), many=True)
        return Response(serializer.data, status=200)


    def post(self, request, *args, **kwargs):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class RecipeFoodView(APIView):
    def get(self, request, id=None, *args, **kwargs):
        if id:
            serializer = RecipeFoodSerializer(RecipeFood.objects.get(id=id))
        else:
            serializer = RecipeFoodSerializer(RecipeFood.objects.all(), many=True)
        return Response(serializer.data, status=200)


    def post(self, request, *args, **kwargs):
        serializer = RecipeFoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class FavoriteView(APIView):
    def get(self, request, id=None, *args, **kwargs):
        if id:
            serializer = FavoriteSerializer(Favorite.objects.get(id=id))
        else:
            serializer = FavoriteSerializer(Favorite.objects.all(), many=True)
        return Response(serializer.data, status=200)


    def post(self, request, *args, **kwargs):
        serializer = FavoriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CategoryView(APIView):
    def get(self, request, id=None, *args, **kwargs):
        if id:
            serializer = CategorySerializer(Category.objects.get(id=id))
        else:
            serializer = CategorySerializer(Category.objects.all(), many=True)
        return Response(serializer.data, status=200)


    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
