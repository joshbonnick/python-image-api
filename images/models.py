from django.db import models


class ImageGeneration(models.Model):
    class ImageType(models.TextChoices):
        SVG = "SVG"

    type = models.CharField(max_length=4, choices=ImageType, db_index=True)
    size = models.JSONField()
    color = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)

    timestamp = models.DateTimeField("date generated")
