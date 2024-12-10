from django.db import models

# Create your models here.
class rooms(models.Model):
    room_id = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=50)  # Add category field
    members = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
