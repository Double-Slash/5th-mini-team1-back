from rest_framework import serializers
from .models import *


class PostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posting
        # fields = ('title', 'content', 'author', 'deadline', 'hashtags', 'field', 'image')
        # exclude = ['password']
        fields = '__all__'


class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        # fields = ('title', 'content', 'author', 'deadline', 'hashtags', 'field', 'image')
        # exclude = ['password']
        fields = '__all__'


    # def create(self, validated_data):
    #     clothing_image = self.context.get("view").request.FILES
    #     instance = self.Meta.model.objects.create(**validated_data)
    #     try:
    #         instance.img = clothing_image['img']
    #     except:
    #         pass
    #     return instance

    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret["images"] = ImageSerializer(instance.images.all(), many=True).data
    #     ret["clothing"] = instance.pk
    #     return ret
