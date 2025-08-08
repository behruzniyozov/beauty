from rest_framework import serializers
from apps.courses.models import Category

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description', 'image']
        extra_kwargs = {
            'name': {'required': True, 'max_length': 255},
            'description': {'required': False, 'allow_blank': True},
            'image': {'required': False, 'allow_null': True}
        }

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    def validate_image(self, value):
        if value and not value.name.lower().endswith(('.png', '.jpg', '.jpeg')):
            raise serializers.ValidationError("Image must be a PNG or JPG file.")
        return value
    

class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description', 'icon']
        extra_kwargs = {
            'name': {'required': True, 'max_length': 255},
            'description': {'required': False, 'allow_blank': True},
            'icon': {'required': False, 'allow_null': True}
        }

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    def validate_icon(self, value):
        if value and not value.name.lower().endswith(('.png', '.jpg', '.jpeg')):
            raise serializers.ValidationError("Icon must be a PNG or JPG file.")
        return value
    
class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'icon']
        extra_kwargs = {
            'id': {'read_only': True},
            'name': {'required': True, 'max_length': 255},
            'description': {'required': False, 'allow_blank': True},
            'icon': {'required': False, 'allow_null': True}
        }

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value
    
    def validate_icon(self, value):
        if value and not value.name.lower().endswith(('.png', '.jpg', '.jpeg')):
            raise serializers.ValidationError("Icon must be a PNG or JPG file.")
        return value
    
class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'icon']
        extra_kwargs = {
            'id': {'read_only': True},
            'name': {'required': True, 'max_length': 255},
            'description': {'required': False, 'allow_blank': True},
            'icon': {'required': False, 'allow_null': True}
        }

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    def validate_icon(self, value):
        if value and not value.name.lower().endswith(('.png', '.jpg', '.jpeg')):
            raise serializers.ValidationError("Icon must be a PNG or JPG file.")
        return value