from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *
User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User

    # def create(self, validated_data):
    #     # print(validated_data)
    #     instance = self.Meta.model.objects.create_user(**validated_data)
    #     return instance




