from django.db import models
from django.contrib.auth import get_user_model
from app.models import BaseModel


User = get_user_model()


class Blog(BaseModel):
    """
    Model to store blogs
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title[:9]
