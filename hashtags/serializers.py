from rest_framework import serializers
from .models import *


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultTag
        fields = '__all__'