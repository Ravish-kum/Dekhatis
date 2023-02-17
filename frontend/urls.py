from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("categories/",views.categories, name='categories'),
    path("categories/description/<str:myid>", views.description, name='description'),
    path('order/', views.order, name='order'),
    path("", views.home, name="home"),
    path("addcart/",views.addcart, name='addcart'),

]