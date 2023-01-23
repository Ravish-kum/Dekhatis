'''
from django.db import models
import string
import random
 # Create your models here.

def generate_unique_code():
    length = 6
    while True:
        code="".join(random.choices(string.ascii_uppercase,k =length))
        if Room.objects.filter(code=code).count() == 0:
            break
    return code
 
class Room(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=122)
    id = models.IntegerField()
    date = models.DateField()
'''
from django.db import models
import string
import random
 # Create your models here.

def generate_unique_code():
    length = 6
    while True:
        code="".join(random.choices(string.ascii_uppercase,k =length))
        if Room.objects.filter(code=code).count() == 0:
            break
    return code
class Room(models.Model):
    serial = models.IntegerField(null= False, default= 1)
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=122)                                        
    date = models.DateTimeField(auto_now_add=True)
