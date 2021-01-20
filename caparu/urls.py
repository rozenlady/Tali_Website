from django.urls import path
from .views import caparu_view

app_name = 'caparu'

urlpatterns = [
    path('', caparu_view, name='caparu-view'),
]
