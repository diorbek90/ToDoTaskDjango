from .models import ToDoItem
from rest_framework import serializers

class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ['id', 'description', 'completed', 'created_at', 'updated_at']