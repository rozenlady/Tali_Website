from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

def cv_view(request):
    return render(request, 'cv/cv.html')