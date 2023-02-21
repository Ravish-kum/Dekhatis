from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("credentials/",views.credentials, name='credentials'),
    path("query/",views.query, name='query')


]