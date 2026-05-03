from django.db import models


class ImageGeneration(models.Model):
    class ImageType(models.TextChoices):
        SVG = "SVG", "Scalable Vector Graphic"

    type = models.CharField(max_length=4, choices=ImageType, db_index=True)
    size = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)

    timestamp = models.DateTimeField("date generated")
