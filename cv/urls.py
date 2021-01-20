from django.urls import path
from .views import cv_view

app_name = 'cv'

urlpatterns = [
    path('', cv_view, name='cv-view'),
]
