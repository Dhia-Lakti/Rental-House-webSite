from dataclasses import fields
from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserResponseSerializer(serializers.ModelSerializer):
    articles = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'mail', 'phone', 'articles', 'image']


class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'mail', 'phone', 'password', 'image']

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :   param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)

    
