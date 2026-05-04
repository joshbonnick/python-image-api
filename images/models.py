import datetime

from django.db import models
from django.utils import timezone


class ImageGeneration(models.Model):
    class ImageType(models.TextChoices):
        SVG = "SVG"

    type = models.CharField(max_length=4, choices=ImageType, db_index=True)
    size = models.JSONField()
    color = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)

    timestamp = models.DateTimeField("date generated")

    def __str__(self):
        return f"{self.type}: {self.size}"

    def was_recently_generated(self):
        return self.timestamp >= timezone.now() - datetime.timedelta(days=1)
