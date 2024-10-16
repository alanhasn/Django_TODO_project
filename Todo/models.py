# models.py
from django.db import models
from django.contrib.auth.models import User

class Todo_list(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)  # Ensure this field is correctly defined

    def __str__(self):
        return self.Title