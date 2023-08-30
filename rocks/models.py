from django.db import models
from django.contrib.auth.models import User


class Rock(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """

    image_filters = [
        ('ammonite', 'ammonite'),
        ('rock', 'rock'),
        ('fossil', 'fossil'),
        ('unknown_rock', 'unknown_rock'),
        ('unknown_fossil', 'unknown_fossil')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    info = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    material = models.CharField(max_length=255, blank=True)
    size = models.CharField(max_length=50, blank=True)
    era = models.CharField(max_length=255, blank=True)
    tools = models.TextField(blank=True)
    found = models.DateTimeField(blank=True)
    prepped = models.BooleanField(blank=False, default=False)

    image = models.ImageField(
        upload_to='images/', default='../default_post_i7zqny', blank=True
    )
    finished_image = models.ImageField(
        upload_to='images/', default='../default_post_i7zqny', blank=True
    )

    image_filter = models.CharField(
        max_length=32, choices=image_filters, default='fossil'
    )

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return f'{self.id} {self.title}'