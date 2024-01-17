from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks', null=True, blank=True)
    #photos = models.ManyToManyField('Photo', related_name='tasks', blank=True)
    image = models.ImageField(upload_to='task_photos/', default='', blank=True,
                              null=True)
    
    def __str__(self):
        return self.title


class Photo(models.Model):
    task = models.ForeignKey(Task, related_name='task_photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='task_photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.task.title} Photo"
 
