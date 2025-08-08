from rest_framework import serializers
from apps.users.models import UserWebinar

class UserWebinarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWebinar
        fields = ('id', 'user', 'webinar', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class UserWebinarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWebinar
        fields = ('id', 'user', 'webinar', 'status', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_status(self, value):
        if value not in ['registered', 'attended', 'missed']:
            raise serializers.ValidationError("Invalid status.")
        return value
    

class UserWebinarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWebinar
        fields = ('user', 'webinar', 'status')
        read_only_fields = ('id', 'created_at', 'updated_at')

class UserWebinarUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWebinar
        fields = ('status',)
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_status(self, value):
        if value not in ['registered', 'attended', 'missed']:
            raise serializers.ValidationError("Invalid status.")
        return value