from django.db import models
from users.models import CustomUser
from projects.models import Project

class Bid(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="bids")
    freelancer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('accepted', 'Accepted')], default='pending')

    def __str__(self):
        return f"{self.freelancer.username} bid on {self.project.title}"
