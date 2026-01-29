from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta


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
    created_by = models.ForeignKey(User, on_delete=models.CASCADE , related_name="tasks")
    created_at =models.DateField(auto_now=True)
    