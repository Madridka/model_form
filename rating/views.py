from django.shortcuts import render, redirect
from django.views.generic.base import View

from .models import Rating
from .forms import *


def add_rating(request):
    if request.method == 'POST':
        form = AddRating(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddRating()
    return render(request, 'index.html', {'form': form})
