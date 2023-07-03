from django.db import models
from django.contrib.auth.models import User
from app.models import BaseModel


class Blog(BaseModel):
    """
    Model to store blogs
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
