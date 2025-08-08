from rest_framework import serializers
from apps.courses.models import Lesson

class LessonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['module', 'title', 'description', 'file', 'duration']
        extra_kwargs = {
            'file': {'required': False, 'allow_null': True}
        }

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_duration(self, value):
        if value.total_seconds() <= 0:
            raise serializers.ValidationError("Duration must be a positive value.")
        return value
    
class LessonUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['module', 'title', 'description', 'file', 'duration']
        extra_kwargs = {
            'file': {'required': False, 'allow_null': True}
        }

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_duration(self, value):
        if value.total_seconds() <= 0:
            raise serializers.ValidationError("Duration must be a positive value.")
        return value
    
class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'module', 'title', 'description', 'file', 'duration']
        read_only_fields = ['id', 'file']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['module'] = instance.module.name if instance.module else None
        return representation
    

class LessonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'module', 'title', 'description', 'file', 'duration']
        read_only_fields = ['id', 'file']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['module'] = instance.module.name if instance.module else None
        return representation