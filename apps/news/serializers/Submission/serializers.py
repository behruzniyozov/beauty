from rest_framework import serializers
from apps.news.models import Submission

class SubmissionListSerializer(serializers.ModelSerializer):
    question_title = serializers.CharField(source='question.title', read_only=True)

    class Meta:
        model = Submission
        fields = ('id', 'user', 'question', 'question_title', 'answer', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

class SubmissionDetailSerializer(serializers.ModelSerializer):
    question_title = serializers.CharField(source='question.title', read_only=True)

    class Meta:
        model = Submission
        fields = ('id', 'user', 'question', 'question_title', 'chosen_option', 'text_answer', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_text_answer(self, value):
        if not value:
            raise serializers.ValidationError("Text answer cannot be empty.")
        return value

    def validate_chosen_option(self, value):
        if not value:
            raise serializers.ValidationError("Chosen option cannot be empty.")
        return value
    
class SubmissionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ('user', 'question', 'chosen_option', 'text_answer')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_text_answer(self, value):
        if not value:
            raise serializers.ValidationError("Text answer cannot be empty.")
        return value

    def validate_chosen_option(self, value):
        if not value:
            raise serializers.ValidationError("Chosen option cannot be empty.")
        return value
    

class SubmissionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ('chosen_option', 'text_answer')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_text_answer(self, value):
        if not value:
            raise serializers.ValidationError("Text answer cannot be empty.")
        return value

    def validate_chosen_option(self, value):
        if not value:
            raise serializers.ValidationError("Chosen option cannot be empty.")
        return value