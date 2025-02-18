from django.urls import path
from .views import cv_view

urlpatterns = [
    path('cv/', cv_view, name='cv'),
]
