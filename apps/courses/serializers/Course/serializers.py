from rest_framework import serializers
from beauty.apps.courses.models import Course

class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['title', 'description', 'price', 'card', 'category', 'author', 'rating']
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
    

    def validate_rating(self, value):
        if value is not None and (value < 0 or value > 5):
            raise serializers.ValidationError("Rating must be between 0 and 5.")
        return value
    

class CourseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['title', 'description', 'price', 'card', 'category', 'author', 'rating']
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
    
    def validate_rating(self, value):
        if value is not None and (value < 0 or value > 5):
            raise serializers.ValidationError("Rating must be between 0 and 5.")
        return value
    
class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price', 'card', 'category', 'author', 'rating']
        read_only_fields = ['id', 'card', 'rating']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = instance.category.name if instance.category else None
        representation['author'] = instance.author.username if instance.author else None
        return representation
    
class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price', 'card', 'category', 'author', 'rating']
        read_only_fields = ['id', 'card', 'rating']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = instance.category.name if instance.category else None
        representation['author'] = instance.author.username if instance.author else None
        return representation
    