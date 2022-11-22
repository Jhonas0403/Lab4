from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Platos,Product
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    title = "Prueba"
    return render(request,'index.html',{"title":title})


def hello(request, id):
    return HttpResponse("<h1>Hola %s</h1>" % id)


def about(request):
    return render(request,'about.html')


def products(request):
    prod =list(Product.objects.values())
    return render(request,'products.html',{'productos':prod})


def create_dish (request):
        return render(request,'create_plato.html')

def platos(request ):
    
    #plato = get_object_or_404(Platos, id = id)
    ##platos = Platos.objects.get(title = title)
    platos = Platos.objects.all()
    print(platos)
    return render(request,'platos.html',{
        'platos': platos
    })