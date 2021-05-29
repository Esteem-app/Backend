from django.db import models

from users.models import MyUser


class Achievement(models.Model):
    content = models.CharField(max_length=255)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
