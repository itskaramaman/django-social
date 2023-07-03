from django.db import models


class BaseModel(models.Model):
    """
    Base Model for all the models of project
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
