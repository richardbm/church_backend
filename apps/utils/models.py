from django.db import models


class CustomModel(models.Model):
    is_active = models.BooleanField(default=True)  # for soft delete
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
