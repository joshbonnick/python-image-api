from django.urls import path

from .views import SvgImages

urlpatterns = [
    path('svg/<path:size>/<path:color>', SvgImages.as_view()),
    path('svg/<path:size>', SvgImages.as_view()),
    path('svg/', SvgImages.as_view()),
]
