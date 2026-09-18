from django.db import models
from django.utils import timezone


class Note(models.Model):

    # CharField = short text (max 200 characters)
    title = models.CharField(max_length=200)
    # TextField = unlimited text length
    content = models.TextField()
    # DateTimeField with auto_now_add=True=automatically sets the time when
    # created
    created_at = models.DateTimeField(auto_now_add=True)
    # DateTimeField with auto_now=True=automatically updates every time we save
    updated_at = models.DateTimeField(auto_now=True)

    # __str__ method = what to display when you print a Note object
    def __str__(self):
        return self.title

    # Meta class = extra configuration for this model
    class Meta:
        ordering = ['-created_at']
# Create your models here.
