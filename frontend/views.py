from django.shortcuts import render, HttpResponse, redirect
from api.models import Product
from api.models import Customer_table
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
 
def home(request, *args, **kwargs):     #def index(request):
    statement = request.POST.get("pin")
    7
    request.session['pin_ava']= statement
    request.session.modified= True
    if request.method =='POST':
        searcher = request.POST.get('search')
        request.session['searching']= searcher
        request.session.modified= True

        return redirect('categories')
    else:
        return render(request,'frontend/home.html')


def categories(request): 
    items = Product.objects.all()
    categoryid = request.GET.get('categories')
    
    #categ= Product.objects.values("item_categories").distinct()

    categoryfilter= request.session['searching']
    if categoryid is not None:
        items = Product.objects.filter(item_categories=categoryid)
    else:   
        if categoryfilter is not None :
            items = Product.objects.filter(item_name__icontains=categoryfilter)

        else :
           items = Product.objects.all()
    
    request.session['searching']= None
    context = {'items':items}
    
    return render(request,'frontend/categories.html',context=context)

def description(request, myid):
    #order_range=Product.objects.values('shop_pin').distinct()
    rangechecker = request.session['pin_ava']
    order_range= Product.objects.values('shop_pin').filter(item_id=myid)   
    order_range= order_range[0]
    order_range= order_range.values()
    order_range= str(list(order_range)[0])

    product = Product.objects.filter(item_id=myid)
    return render(request, 'frontend/description.html',{'product':product[0], 'order_range':order_range,'rangechecker':rangechecker})


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

def addcart(request):
    cartfillings = request.POST.get("cartproduct")
    cart= request.session.get('cart')

    if  cart:
        quantity = cart.get(cartfillings)
        if quantity:
            cart[cartfillings]= quantity + 1
        else:
            cart[cartfillings]=1
    else:
        cart={}
        cart[cartfillings]=1

    request.session['cart'] = cart
    things = list(request.session.get('cart').keys())
    cart_items= Product.objects.filter(item_id__in=things)
    if request.method =='POST':
        return render(request, 'frontend/cart.html', {'cart_items':cart_items})
    return redirect('categories')