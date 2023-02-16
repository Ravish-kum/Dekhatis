from django.shortcuts import render, HttpResponse, redirect
from api.models import Product
from api.models import Customer_table
from django.contrib.auth.decorators import login_required

# Create your views here.
 
def home(request, *args, **kwargs):     #def index(request):

    if request.method =='POST':
        searcher = request.POST.get('search')
        request.session['searching']= searcher
        request.session.modified= True

        return redirect('categories')
    else:
        return render(request,'frontend/home.html')

@login_required

def categories(request): 
    items = Product.objects.all()
#----------------------------------------------------------------------------
    statement = request.POST.get("pin")
    request.session['pin_ava']= None
    if statement is None and request.session['pin_ava'] is not None:
        statement = request.session['pin_ava']

    request.session['pin_ava']= statement
#------------------------------------------------------------------------------
    #categ= Product.objects.values("item_categories").distinct()
    categoryid = request.GET.get('categories')
#------------------------------------------------------------------------------
    cartfillings = request.POST.get("cartproduct")
    cart= request.session['cart'] 

    print(cartfillings)

    if  cart:
        quantity = cart.get(cartfillings)
        if quantity:
            cart[cartfillings]= quantity + 1
        else:
            cart[cartfillings]=1
    else:
        cart={}
        cart[cartfillings]=1

    request.session['cart']= cart


    print('cart',request.session['cart'])

    #--------------------------------------------------------------------------
    request.session['searching']=None
    categoryfilter= request.session['searching']
    if categoryid is not None:
        items = Product.objects.filter(item_categories=categoryid)
    else:   
        if categoryfilter is not None :
            items = Product.objects.filter(item_name__icontains=categoryfilter)

        else :
           items = Product.objects.all()

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
