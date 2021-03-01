from django.db import models

# Create your models here.

class TVshows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=30)
    releaseDate = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
