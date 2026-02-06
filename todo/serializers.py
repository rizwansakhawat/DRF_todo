from rest_framework import serializers
from .models import Task, Category
from datetime import date
from django.contrib.auth.models import User

class UserSerializer1(serializers.ModelSerializer):
    # tasks = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name= 'task_detail')
    # # tasks = serializers.SlugRelatedField(
    # #     many=True,
    # #     read_only=True,
    # #     slug_field='title'
    # #  )

    # # tasks = serializers.PrimaryKeyRelatedField(
    # #     many=True, queryset=Task.objects.all()
    # # )
    class Meta:
        model = User
        fields = ["id", "username"]
        
        



class TaskSerializer(serializers.ModelSerializer):
    # owner = serializers.StringRelatedField(source="owner.username")
    owner = UserSerializer1(read_only = True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    
    url = serializers.HyperlinkedIdentityField(view_name="task_detail", read_only=True)
    
    
    def validate_due_date(self, value):
        """
        Validate that due_date is not in the past
        """
        if value < date.today():
            raise serializers.ValidationError("Due date cannot be in te past")
        return value

    
    class Meta:
        model = Task
        fields = ["id", "url", "title", 'due_date', "order" ,"content",  "status" ,  "owner" , "category" , "created_at"]
        read_only_fields = ["id","owner",  "created_at"]
        
        
class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name= 'task_detail')
    # # tasks = serializers.SlugRelatedField(
    # #     many=True,
    # #     read_only=True,
    # #     slug_field='title'
    # #  )

    # # tasks = serializers.PrimaryKeyRelatedField(
    # #     many=True, queryset=Task.objects.all()
    # # )
    
    # tasks = TaskSerializer(many=True, read_only=True)


    class Meta:
        model = User
        fields = ["id", "username", "tasks"]
        
        
class CaterorySerializer(serializers.ModelSerializer):
    # tasks = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='task_detail')
    # tasks = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    # tasks = serializers.PrimaryKeyRelatedField(many=True , read_only=True)
    
    tasks= TaskSerializer(many=True, read_only=True)
    


    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'user' , 'tasks']
    
    # def create(self, validated_data):
    #     task_data = validated_data.pop('tasks')
    #     category = Task.objects.create(**validated_data)
    #     for task_data in task_data:
    #         Task.objects.create(category=category, **task_data)
    
    #     return category
