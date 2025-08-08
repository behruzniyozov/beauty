from rest_framework import serializers
from apps.courses.models import Comment

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user','course', 'webinar', 'text', 'rating']
        extra_kwargs = {
            'user': {'read_only': True},
            'course': {'required': False, 'allow_null': True},
            'webinar': {'required': False, 'allow_null': True},
            'rating': {'required': False, 'allow_null': True}
        }

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Content cannot be empty.")
        return value
    
    def validate_rating(self, value):
        if value is not None and (value < 1 or value > 5):
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value
    
class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'course', 'webinar', 'text', 'rating', ]
        read_only_fields = ['id', 'created_at']
        extra_kwargs = {
            'course': {'required': False, 'allow_null': True},
            'webinar': {'required': False, 'allow_null': True},
            'rating': {'required': False, 'allow_null': True}
        }

class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text', 'rating']
        extra_kwargs = {
            'text': {'required': True},
            'rating': {'required': False, 'allow_null': True}
        }

    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError("Text cannot be empty.")
        return value
    def validate_rating(self, value):
        if value is not None and (value < 1 or value > 5):
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value
    

class CommentDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'course', 'webinar', 'text', 'rating']
        read_only_fields = ['id', 'created_at']
        extra_kwargs = {
            'course': {'required': False, 'allow_null': True},
            'webinar': {'required': False, 'allow_null': True},
            'rating': {'required': False, 'allow_null': True}
        }   

        
    
