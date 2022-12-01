from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    ownerName = serializers.CharField(source="owner.username", read_only=True)
    ownerImage = serializers.CharField(source="owner.image", read_only=True)
    ownerPhone = serializers.CharField(source="owner.phone", read_only=True)
    ownerEmail = serializers.CharField(source="owner.mail", read_only=True)
    class Meta:
        model = Article
        fields = ['id', 'owner', 'title', 'description', 'price', 'images', 'type', 'ownerName', 'ownerImage', 'ownerEmail', 'ownerPhone']