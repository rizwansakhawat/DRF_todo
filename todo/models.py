from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta


class Category(models.Model):    
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['created_at']


class Task(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'pending'),
        ('PROGRESS', 'progress'),
        ('COMPLETED', 'completed')
        
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    due_date = models.DateField()
    order = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE , related_name="tasks") 
    owner = models.ForeignKey(User, on_delete=models.CASCADE , related_name="tasks")
    created_at =models.DateField(auto_now_add=True)
    
    
    
    
    
    
    class Meta:
        unique_together = ['category', 'order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)
    