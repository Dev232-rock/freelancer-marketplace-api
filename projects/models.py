from django.db import models
from users.models import CustomUser

class Project(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="posted_projects")
    title = models.CharField(max_length=255)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ]
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return self.title
