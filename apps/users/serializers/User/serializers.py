from rest_framework import serializers
from apps.users.models import User

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_username(self, value):
        if not value:
            raise serializers.ValidationError("Username cannot be empty.")
        return value

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email cannot be empty.")
        return value
    
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_username(self, value):
        if not value:
            raise serializers.ValidationError("Username cannot be empty.")
        return value

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email cannot be empty.")
        return value

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_username(self, value):
        if not value:
            raise serializers.ValidationError("Username cannot be empty.")
        return value

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email cannot be empty.")
        return value
    
