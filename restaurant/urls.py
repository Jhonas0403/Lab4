from django.urls import path

from . import views

urlpatterns =[
     path('',views.index),
    path('about/',views.about),
    path('hello/<int:id>',views.hello),
    path('productos/',views.products),
    path('platos/',views.platos),
    path('createDish/',views.create_dish)
]