from django.apps import AppConfig
from django.contrib import admin

class ImagesConfig(AppConfig):
    name = 'images'

    def ready(self):
        from .models import ImageGeneration
        admin.site.register(ImageGeneration)
