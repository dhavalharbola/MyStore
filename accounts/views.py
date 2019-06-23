from django.shortcuts import render,redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User 
from django.contrib import messages

def sign_up(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        
        # password checking
        if password==password2:
                #user name and email cheking
            if User.objects.filter(username=username).exists():
                messages.error(request,'This username is alredy taken,please try a new one')
                return redirect('sign_up')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'This Email is alredy taken,please try a new one')
                    return redirect('sign_up')
                else:
                    user=User.objects.create_user(username=username,email=email,
                    password=password,first_name=first_name,last_name=last_name)  
                    user.save()
                    messages.success(request,'Registration Successful.You can Log In ')
                    return redirect('log_in') 

        else:
            messages.error(request,'password do not match')
            return redirect('sign_up')
    else:
        return render(request,'accounts/signup.html')

 


def log_in(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            
            return redirect('shop:product_list')
        else:
            messages.error(request,'Inavalid Credentials') 
            return redirect('log_in') 

    else:  
        return render(request,'accounts/login.html') 


def log_out(request):

    logout(request)

    return redirect('shop:product_list')
    
