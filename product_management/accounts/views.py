from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from  django.contrib import auth

# Create your views here.


def register(request):
    if request.method=='POST':
        username=request.POST['username']  #janu
        email=request.POST['Email']
        password1=request.POST['Password']
        password2=request.POST['Password2']

        if password1 == password2: #relation  opertion or comparision
            if User.objects.filter(username=username).exists():
                print('username Exists....')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    print('Email is already taken ,Try another one')
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,email=email,password=password1)
                    user.save() # send the data to the datad base and tabile
                    return redirect('login')
        else:
            print('password did not match')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')
    

def login(request):
    if request.method=='POST':  # if the condition is true it should be enter into the if condition
        username=request.POST['username'] 
        password=request.POST['Password']

        user=auth.authenticate(username=username,password=password)

        if User is not None:
            auth.login(request,user)
            print('Login success...')
            return redirect('ShowProducts')
        else:
            print('Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')
    

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        print("Logout From webside...")
        return redirect('login')