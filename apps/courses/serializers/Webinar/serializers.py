from rest_framework import serializers
from apps.courses.models import Webinar

class WebinarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinar
        fields = ['title', 'description', 'price', 'card', 'category', 'author', 'datetime', 'rating']
        extra_kwargs = {
            'card': {'required': False, 'allow_null': True},
            'rating': {'required': False, 'allow_null': True}
        }

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative.")
        return value
    
class WebinarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinar
        fields = ['id', 'title', 'description', 'price', 'card', 'category', 'author', 'datetime', 'rating']
        read_only_fields = ['id']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category_name'] = instance.category.name
        representation['author_name'] = instance.author.username
        return representation
    
class WebinarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinar
        fields = ['id', 'title', 'description', 'price', 'card', 'category', 'author', 'datetime', 'rating']
        read_only_fields = ['id']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category_name'] = instance.category.name
        representation['author_name'] = instance.author.username
        return representation

class WebinarUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinar
        fields = ['title', 'description', 'price', 'card', 'category', 'author', 'datetime', 'rating']
        extra_kwargs = {
            'card': {'required': False, 'allow_null': True},
            'rating': {'required': False, 'allow_null': True}
        }

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative.")
        return value