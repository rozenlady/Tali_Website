from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

def dbt_view(request):
    return render(request, 'dbt/dbt.html')