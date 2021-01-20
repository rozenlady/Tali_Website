from django.urls import path
from .views import dbt_view

app_name = 'dbt'

urlpatterns = [
    path('', dbt_view, name='dbt-view'),
]
