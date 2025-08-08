from rest_framework import serializers
from apps.users.models import Interest

class InterestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ('id', 'name', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

class InterestDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    def validate_description(self, value):
        if not value:
            raise serializers.ValidationError("Description cannot be empty.")
        return value
    
class InterestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ('name', 'description')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    def validate_description(self, value):
        if not value:
            raise serializers.ValidationError("Description cannot be empty.")
        return value
    
class InterestUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ('name', 'description')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    def validate_description(self, value):
        if not value:
            raise serializers.ValidationError("Description cannot be empty.")
        return value