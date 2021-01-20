from django.urls import path
from .views import tftsd_view

app_name = 'tftsd'

urlpatterns = [
    path('', tftsd_view, name='tftsd-view'),
]
