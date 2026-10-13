from django.db import models
from users.models import User

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:30]}"
    