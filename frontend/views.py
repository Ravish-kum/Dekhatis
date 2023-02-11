from django.shortcuts import render, HttpResponse, redirect
from api.models import Product
from api.models import Customer_table
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request, *args, **kwargs):     #def index(request): 
    return render(request,'frontend/index.html')

def test(request):
    global statement
    items = Product.objects.all()
    categ= Product.objects.values("item_categories").distinct()
    categoryid=request.GET.get('categories')
    statement=request.POST.get('pin')
    if categoryid is None:
        items = Product.objects.all()
    else :
        items = Product.objects.filter(item_categories=categoryid)

    context = {'items':items,'categ':categ }
    return render(request,'frontend/test.html',context=context)

def description(request, myid):
    #order_range=Product.objects.values('shop_pin').distinct()

    order_range= Product.objects.values('shop_pin').filter(item_id=myid)   

    order_range= order_range[0]
    order_range= order_range.values()
    order_range= str(list(order_range)[0])

    product = Product.objects.filter(item_id=myid)
    return render(request, 'frontend/description.html',{'product':product[0], 'order_range':order_range,'statement':statement})


#---------------------------------------order------------------------------------------------------------
def order(request): 
    
    if request.method == 'GET': 
        return render(request,'frontend/credentials.html')
    else: 
        postdata =request.POST
        name = postdata.get('name')
        phone= postdata.get('phone')
        address = postdata.get('address')
        pin = postdata.get('pin')
        email= postdata.get('email')
        password= postdata.get('password')
        customer= Customer_table(
                           customer_name=name,
                           customer_phone=phone,
                           customer_address=address,
                           customer_pin=pin,
                           customer_email=email,
                           customer_pass=password
                           )
        customer.save()     
        return redirect('test')
