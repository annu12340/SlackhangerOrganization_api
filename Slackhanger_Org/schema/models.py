from django.db import models
from django.contrib.auth.models import User


class Schema(models.Model):
    dress_type = models.CharField(max_length=100)
    schema_format = models.JSONField()
    organization = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Schema: ' + self.dress_type

