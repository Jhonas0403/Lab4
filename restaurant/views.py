from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import DishForm, ProductForm
from .models import Platos, Product


# Create your views here.


def index(request):
    title = "Prueba"
    return render(request, 'index.html', {"title": title})


def hello(request, id):
    return HttpResponse("<h1>Hola %s</h1>" % id)


def about(request):
    return render(request, 'about.html')


def products(request):
    prod = list(Product.objects.values())
    return render(request, 'products.html', {'productos': prod})


def create_dish(request):
    return render(request, 'create_plato.html')


# Create your views here.
def save_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/platos/')

    else:
        form = DishForm()

    return render(request, 'create_plato.html', {'form': form})


def save_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/productos/')

    else:
        form = ProductForm()

    return render(request, 'create_product.html', {'form': form})


def platos(request):
    platos = Platos.objects.all()

    for plato in platos:
        for product in plato.producto.all():
            print(f'Plato %, producto %', plato, product)

    return render(request, 'platos.html', {
        'platos': platos
    })
