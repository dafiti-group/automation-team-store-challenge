import csv, io
from django.shortcuts import render
from django.contrib import messages
from django.views import generic
import pandas as pd
from tablib import Dataset
from django.shortcuts import get_object_or_404
from .models import Shoe

def index(request):

    shoes = Shoe.objects.all()

    return render(request, 'index.html', {'shoes': shoes})

def feminine_shoes(request):

    shoes = Shoe.objects.filter(type__icontains='Feminino')

    # Render the HTML template feminine_shoes.html with the data in the context variable
    return render(request, 'feminine_shoes.html', {'shoes': shoes})

def masculine_shoes(request):

    shoes = Shoe.objects.filter(type__icontains='Masculino')

    # Render the HTML template feminine_shoes.html with the data in the context variable
    return render(request, 'masculine_shoes.html', {'shoes': shoes})


def shoes_detail(request, id):
    shoes = get_object_or_404(Shoe, pk=id)
    return render(request, 'shoe_detail.html', {'shoes': shoes})
