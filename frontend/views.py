from django.shortcuts import render, HttpResponse, redirect
from api.models import Product
from api.models import Images_table
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
    product = Product.objects.filter(item_id=myid)
    #------------------------------------------------------------------------
    if request.method == 'POST':                            # holding pin from description
        statement = request.POST.get("pin")
        request.session['pin_ava'] = statement  
    rangechecker = request.session['pin_ava']                  # rankchecker variable for holding session value
    order_range= Product.objects.values('shop_pin').filter(item_id=myid)   
    order_range= order_range[0]
    order_range= order_range.values()
    order_range= str(list(order_range)[0])                 #order_range variable for geting pin of product
    #------------------------------------------------------------------------
    m_item_id_ofProduct = Product.objects.values('m_item_id').filter(item_id=myid)   #getting varient id 
    varient = None

    try:
        varient_of = m_item_id_ofProduct[0]['m_item_id'].split("#")[2]
        varient = Product.objects.filter(m_item_id__icontains=varient_of).exclude(item_id=myid)
    except:
        pass
    #------------------------------------------------------------------------------
    visualsimilar = Product.objects.filter(item_visual_similarity='visual-'+myid).exclude(item_id=myid)

    #-------------------------------------------------------------------------------
    subject_images=Images_table.objects.filter(item_id=myid)                           #getting more images
    if len(subject_images) !=0 :
        imagesUrl = []
        for i in subject_images:
            for attr, value in i.__dict__.items():
                if value != "":
                    imagesUrl.append(value)
        del imagesUrl[0:3]
        if varient is not None :
            return render(request, 'frontend/description.html', {'product':product[0], 'order_range':order_range,'rangechecker':rangechecker,'imageUrl':imagesUrl,'varient':varient,'visualsimilar':visualsimilar})
        else:
            return render(request, 'frontend/description.html', {'product':product[0], 'order_range':order_range,'rangechecker':rangechecker,'imageUrl':imagesUrl,'visualsimilar':visualsimilar})


    #------------------------------------------------------------------------
    
    return render(request, 'frontend/description.html',{'product':product[0]})



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
        if request.session.get('cart') is not None:    
            things = list(request.session.get('cart').keys())       #fetching id as keys of dict cart
            cart_items= Product.objects.filter(item_id__in=things)  #converting id to json object from data base
        else:
            cart_items = 'nothing present'
        return render(request, 'frontend/cart.html', {'cart_items':cart_items,'number':1})

#------------------------------------------------cart------------------------------------------------------------------------

class Orignalcart(View):
    def get(self, request):
        #quantity = request.session.get('number')
        things = list(request.session.get('cart').keys())       #fetching id as keys of dict cart
        cart_items= Product.objects.filter(item_id__in=things)  #converting id to json object from data base
        return render(request, 'frontend/cart.html', {'cart_items':cart_items,'number':1})
    


