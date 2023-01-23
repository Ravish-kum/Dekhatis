from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializer import RoomSerializer
from .models import Room
'''
# Create your views here.
def main(request):
    return HttpResponse("hello")
'''
class RoomView(generics.CreateAPIView):
    qureyset = Room.objects.all()
    serializeR_Class = RoomSerializer
