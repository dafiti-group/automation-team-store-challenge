from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import FormView, UpdateView, DeleteView
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


class ShoeFormView(FormView):

    form_class = ShoeForm

    template_name = 'shoe_form.html'

    def form_valid(self, form):

        form.save()
        return HttpResponseRedirect(reverse('myapp:index'))

    success_url = "../"



class ShoeUpdateView(UpdateView):

    model = Shoe
    form_class = ShoeForm

    template_name = 'shoes_update.html'

    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('myapp:index')


class ShoeDeleteView(DeleteView):

    model = Shoe

    template_name = 'shoes_delete.html'

    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('myapp:index')
