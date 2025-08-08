from rest_framework import serializers
from apps.courses.models import Module

class ModuleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['course', 'name', 'icon']
        extra_kwargs = {
            'icon': {'required': False, 'allow_null': True}
        }

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value
    


class ModuleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'course', 'name', 'icon']
        read_only_fields = ['id', 'course']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['course_name'] = instance.course.name
        return representation
    
class ModuleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'course', 'name', 'icon']
        read_only_fields = ['id', 'course']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['course_name'] = instance.course.name
        return representation
    
class ModuleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['name', 'icon']
        extra_kwargs = {
            'icon': {'required': False, 'allow_null': True}
        }

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value