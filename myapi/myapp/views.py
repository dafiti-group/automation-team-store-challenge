from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Shoe
from .forms import ShoeForm


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

    return render(request, 'shoes_detail.html', {'shoes': shoes})


def add_shoes(request):

    if request.method == "POST":

        form = ShoeForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()
            print('sucess')

            return HttpResponseRedirect(reverse('myapp:index'))

        else:

            print('failure')
    else:

        form = ShoeForm()

    return render(request, 'add_shoes.html', {'form': form})
