from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200, required=True)
    content = serializers.CharField(required=True)
    
    class Meta:
        model = Task
        fields = ["id", "title", "content", "created_at"]
        read_only_fields = ["id", "created_at"]
        
        
        


