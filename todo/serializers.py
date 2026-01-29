from rest_framework import serializers
from .models import Task
from datetime import date
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    def validate_due_date(self, value):
        """
        Validate that due_date is not in the past
        """
        if value < date.today():
            raise serializers.ValidationError("Due date cannot be in te past")
        return value

    
    class Meta:
        model = Task
        fields = ["id", "title", 'due_date', "content",  "status" ,  "created_by" , "created_at"]
        read_only_fields = ["id", "created_at"]
        
class UserSerializer(serializers.ModelSerializer):
    # tasks = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Task.objects.all()
    # )
    tasks = TaskSerializer(many=True, read_only=True)


    class Meta:
        model = User
        fields = ["id", "username", "tasks"]





        
    
        


