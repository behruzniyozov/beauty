from rest_framework import serializers
from apps.news.models import QuestionOption, Question

class QuestionOptionListSerializer(serializers.ModelSerializer):
    question_title = serializers.CharField(source='question.title', read_only=True)

    class Meta:
        model = QuestionOption
        fields = ('id', 'question', 'question_title', 'text', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class QuestionOptionDetailSerializer(serializers.ModelSerializer):
    question_title = serializers.CharField(source='question.title', read_only=True)

    class Meta:
        model = QuestionOption
        fields = ('id', 'question', 'question_title', 'text', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_text(self, value):
        if not value:
            raise serializers.ValidationError("Text cannot be empty.")
        return value
    
class QuestionOptionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = ('question', 'text')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_text(self, value):
        if not value:
            raise serializers.ValidationError("Text cannot be empty.")
        return value
    
class QuestionOptionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = ('text',)
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_text(self, value):
        if not value:
            raise serializers.ValidationError("Text cannot be empty.")
        return value