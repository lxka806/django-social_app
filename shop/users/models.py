from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, default="")
    email = models.EmailField()
    password = models.CharField(max_length=100, default="")
    is_current_user = models.BooleanField(default=0)
