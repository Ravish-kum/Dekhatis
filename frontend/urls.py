from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.test, name='test'),
    path("frontend/description/<str:myid>", views.description, name='product'),
    path("text/",views.index, name='index'),
    path('order/', views.order, name='order'),



]