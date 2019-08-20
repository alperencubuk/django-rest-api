from django.contrib.auth.models import User
from rest_framework import serializers
from app.alp.models import MyUser


class MyUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ('name', 'street')
