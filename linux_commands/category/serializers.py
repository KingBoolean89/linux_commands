from .models import Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    commands = serializers.StringRelatedField(many=True)
    class Meta:
        model = Category
        fields = ['name', 'commands']