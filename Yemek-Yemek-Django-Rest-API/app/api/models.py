from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)

    class Meta:
        db_table = 'user'


class Food(models.Model):
    name = models.CharField(max_length=64)
    image = models.CharField(max_length=128)
    calorie = models.IntegerField(default=0)
    carbohydrate = models.FloatField(default=0)
    protein = models.FloatField(default=0)
    fat = models.FloatField(default=0)
    health_point = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField()

    class Meta:
        db_table = 'food'


class Recipe(models.Model):
    name = models.CharField(max_length=64)
    image = models.CharField(max_length=128)
    rating = models.IntegerField(default=0)
    calorie = models.IntegerField(default=0)
    carbohydrate = models.FloatField(default=0)
    protein = models.FloatField(default=0)
    fat = models.FloatField(default=0)
    cooking_minutes = models.IntegerField(default=0)
    description = models.TextField()

    class Meta:
        db_table = 'recipe'


class RecipeFood(models.Model):
    recipe_id = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    food_id = models.ForeignKey('Food', on_delete=models.CASCADE)

    class Meta:
        db_table = 'recipe_food'


class Favorite(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    recipe_id = models.ForeignKey('Recipe', on_delete=models.CASCADE)

    class Meta:
        db_table = 'favorite'


class Category(models.Model):
    category = models.CharField(max_length=64)

    class Meta:
        db_table = 'category'
