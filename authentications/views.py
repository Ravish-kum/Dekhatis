from django.shortcuts import render, HttpResponse, redirect
from api.models import Product
from api.models import Customer_table
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here

#--------------------------------authentications---------------------------------------------------------

def signup(request): 
    
    if request.method == 'GET': 
        return render(request,'signup.html')
    else: 
        postdata =request.POST
        name = postdata.get('name')
        email= postdata.get('email')
        password= postdata.get('password')
        password2=postdata.get('password2')
        myuser = User.objects.create_user(name, email, password) 
        myuser.first_name = name
        myuser.save()                   
        messages.success(request, 'your account has been created')
        return redirect('authentications:signin')

def signin(request): 
    if request.method =='POST':
        name= request.POST['name']
        password= request.POST['password']

        user= authenticate(username= name, password= password)

        if user is not None:
            login(request, user)
            name=user.first_name
            #return render(request, 'frontend/home.html', {'name':name})
            return redirect('/')
        else:
            messages.error(request, "bad credentials")

    return render(request,'signin.html')

def signout(request):
    request.session.clear()
    logout(request)
    messages.success(request, "logged out successfully")
    return redirect("home")

def changepassword(request):
    if request.method == "POST":
        name = request.POST.get('name')
        new_password = request.POST.get('new_password')
        u = User.objects.get(username__exact=name)
        u.set_password(new_password)
        u.save()
        messages.success(request, 'your password has been changed')
        return redirect('authentications:signin')

    return render(request, 'changepassword.html')