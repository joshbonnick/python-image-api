from django.urls import path

from .views import SvgImages

urlpatterns = [
    path('svg/<str:size>/<str:color>', SvgImages.as_view()),
    path('svg/<str:size>', SvgImages.as_view()),
    path('svg/', SvgImages.as_view()),
]
