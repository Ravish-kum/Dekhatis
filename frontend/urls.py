from django.contrib import admin
from django.urls import path, include
from . import views
from .views import Addcart
from .views import Orignalcart


urlpatterns = [
    path("categories/",views.categories, name='categories'),
    path("categories/description/<str:myid>", views.description, name='description'),
    path("orignalcart/",Orignalcart.as_view(), name='orignalcart'),
    path("", views.home, name="home"),
    path("addcart/",Addcart.as_view(), name='addcart'),

]