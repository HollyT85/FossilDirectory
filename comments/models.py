from django.db import models
from django.contrib.auth.models import User
from rocks.models import Rock


class RockComments(models.Model):
    """
    Comment model, related to User and Post
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    rock_post = models.ForeignKey(Rock, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content