from rest_framework import serializers
from apps.users.models import UserCourse

class UserCourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        fields = ('id', 'user', 'course', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

class UserCourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        fields = ('id', 'user', 'course', 'status', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_status(self, value):
        if value not in ['enrolled', 'completed', 'dropped']:
            raise serializers.ValidationError("Invalid status.")
        return value
    
class UserCourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        fields = ('user', 'course', 'status')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_status(self, value):
        if value not in ['enrolled', 'completed', 'dropped']:
            raise serializers.ValidationError("Invalid status.")
        return value
    
class UserCourseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        fields = ('status',)
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_status(self, value):
        if value not in ['enrolled', 'completed', 'dropped']:
            raise serializers.ValidationError("Invalid status.")
        return value
    
