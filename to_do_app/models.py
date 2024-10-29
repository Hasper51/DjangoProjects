from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=(('active', 'active'), ('completed', 'completed')), max_length=10, default='active')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title