from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import FormView, UpdateView, DeleteView
from .models import Shoe
from .forms import ShoeForm


def index(request):

    """
    View representing the main page with list of all products
    """

    shoes = Shoe.objects.all()

    return render(request, 'index.html', {'shoes': shoes})


def feminine_shoes(request):

    """
    View representing the page of feminine shoes only
    """

    shoes = Shoe.objects.filter(type__icontains='Feminino')

    return render(request, 'feminine_shoes.html', {'shoes': shoes})


def masculine_shoes(request):

    """
    View representing the page of masculine shoes only
    """

    shoes = Shoe.objects.filter(type__icontains='Masculino')

    return render(request, 'masculine_shoes.html', {'shoes': shoes})


def shoes_detail(request, id):

    """
    View with detail info about each product
    """

    shoes = get_object_or_404(Shoe, pk=id)

    return render(request, 'shoes_detail.html', {'shoes': shoes})


class ShoeFormView(FormView):

    """
    Form view for the user's input when creating a new product
    """

    form_class = ShoeForm
    template_name = 'shoe_form.html'

    def form_valid(self, form):

        form.save()
        return HttpResponseRedirect(reverse('myapp:index'))

    success_url = "../"



class ShoeUpdateView(UpdateView):

    """
    View where the user can update a existing product
    """

    model = Shoe
    form_class = ShoeForm
    template_name = 'shoes_update.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('myapp:index')


class ShoeDeleteView(DeleteView):

    """
    View where the user can delete a existing product
    """

    model = Shoe
    template_name = 'shoes_delete.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('myapp:index')
