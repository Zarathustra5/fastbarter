from rest_framework import serializers
from .models import Catalog

class CatalogSerializer(serializers.Serializer):
    photo = serializers.ImageField(read_only=True)
    title = serializers.CharField(max_length=255)
    short_desc = serializers.CharField()
    price = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    category_id = serializers.IntegerField()
    category_exchange_id = serializers.IntegerField(read_only=True)
    is_published = serializers.BooleanField(read_only=True)
    is_favorite = serializers.BooleanField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)