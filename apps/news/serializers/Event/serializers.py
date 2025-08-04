from rest_framework import serializers
from beauty.apps.news.models import Event

class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'card', 'datetime', 'location_name']
        read_only_fields = ['id']


class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'card', 'datetime', 'location_name', 'longitude', 'latitude']
        read_only_fields = ['id']

class EventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'description', 'card', 'datetime', 'location_name', 'longitude', 'latitude']
        read_only_fields = []
    
    def create(self, validated_data):
        return Event.objects.create(**validated_data)
        

class EventUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'description', 'card', 'datetime', 'location_name', 'longitude', 'latitude']
        read_only_fields = []
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.card = validated_data.get('card', instance.card)
        instance.datetime = validated_data.get('datetime', instance.datetime)
        instance.location_name = validated_data.get('location_name', instance.location_name)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.save()
        return instance