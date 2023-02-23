from django.shortcuts import render, HttpResponse, redirect
from api.models import Product
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views import View
# Create your views here.

# -------------------------------------------------home------------------------------------------------------------------------------

def home(request, *args, **kwargs):  

    statement = request.POST.get("pin")                     #statement variable for pin
    request.session['pin_ava']= statement
    request.session.modified= True
    request.session['searching']=None
    if request.method =='POST':                             #searcher variable for searching name
        searcher = request.POST.get('search')
        if searcher is not None :
            request.session['searching']= searcher
            request.session.modified= True
        else:
            request.session['searching']= None
        return redirect('categories')
    else:
        return render(request,'frontend/home.html')

#------------------------------------------------categories--------------------------------------------------------------------------

def categories(request): 
    print(request.session['searching'])
    items = Product.objects.all()                                       #items contains all products from item table 
    categoryid = request.GET.get('categories')                          #categoryid variable get the category clicked on bar
    categoryfilter= request.session['searching']                        #categoryfilter -- session declaration 
    if categoryid is not None:
        items = Product.objects.filter(item_categories=categoryid)
    else:   
        if categoryfilter is not None :
            items = Product.objects.filter(item_name__icontains=categoryfilter)
        else :
           request.session['searching']= None
           items = Product.objects.all()

    context = {'items':items}
    
    return render(request,'frontend/categories.html',context=context)   #categ= Product.objects.values("item_categories").distinct()

#------------------------------------------------description-------------------------------------------------------------------------

def description(request, myid):
    
    if request.method == 'POST':                            # holding pin from description
        statement = request.POST.get("pin")
        request.session['pin_ava'] = statement  
    rangechecker = request.session['pin_ava']                  # rankchecker variable for holding session value
    order_range= Product.objects.values('shop_pin').filter(item_id=myid)   
    order_range= order_range[0]
    order_range= order_range.values()
    order_range= str(list(order_range)[0])                      #order_range variable for geting pin of product

    product = Product.objects.filter(item_id=myid)              #product filteration on id
    return render(request, 'frontend/description.html',{'product':product[0], 'order_range':order_range,'rangechecker':rangechecker})




#---------------------------------------------------cart-logic------------------------------------------------------------------------
class Addcart(View):
    def post(self,request):
        cartfillings = request.POST.get("cartproduct")      #cart id getting
        cart= request.session.get('cart')                   #making a dict session

        if  cart:                                           
            quantity = cart.get(cartfillings)                #if cart exsist getting quantity as value of id as key      
            if quantity:
                cart[cartfillings]= quantity + 1 
            else:
                cart[cartfillings]=1
        else:
            cart={}
            cart[cartfillings]=1
        number = cart[cartfillings]                     #fetching key or quantity of a item
        request.session['cart'] = cart
        print(request.session['cart'])
       # request.session['number'] = number
        #request.session.modified= True
        return redirect('orignalcart')
    def get(self,request):
        things = list(request.session.get('cart').keys())       #fetching id as keys of dict cart
        cart_items= Product.objects.filter(item_id__in=things)  #converting id to json object from data base
        return render(request, 'frontend/cart.html', {'cart_items':cart_items,'number':1})

#------------------------------------------------cart------------------------------------------------------------------------

class Orignalcart(View):
    def get(self, request):
        #quantity = request.session.get('number')
        things = list(request.session.get('cart').keys())       #fetching id as keys of dict cart
        cart_items= Product.objects.filter(item_id__in=things)  #converting id to json object from data base
        return render(request, 'frontend/cart.html', {'cart_items':cart_items,'number':1})
    


