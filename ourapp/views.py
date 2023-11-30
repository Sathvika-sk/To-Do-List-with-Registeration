from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from new.settings import EMAIL_HOST_USER
from django.contrib.auth import login,logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from ourapp.models import newuser
from ourapp.backends import EmailBackend
import random
import logging
from django.contrib.auth.hashers import make_password
from django_otp.plugins.otp_totp.models import TOTPDevice
def home(request):
    return render(request,"home.html")
def userlogin(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email,password)
        pas=password
        e=newuser.objects.get(email="shashikiran.24apr@gmail.com")
        print(e.password)
        #print(get_user_model.objects.get(email=email))
        k= EmailBackend.authenticate(email=email,password=pas)
        print(k)
        if k is not None:
            login(request,k)
            print("yes")
            #if request.POST.get('is_verified')=="0": 
            return redirect("/verify/")
        else:
                messages.info(request,"invalid credentials")
                print("not womr")
                return redirect("/userlogin/")
    else:
        return render(request,"userlogin.html")


def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dob=request.POST['dob']
        gender=request.POST['gender']
        highestqualification=request.POST['highestqualification']
        specialisation=request.POST['specialisation']
        address= request.POST['address']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if password1==password2:
            #if newuser.objects.filter(email=email).count()>=1:
                #messages.info(request,'Username Exists! Use a different username.')
                #return redirect('/signup')
            newu=newuser(email=email,first_name=first_name,last_name=last_name,dob=dob,gender=gender,highestqualification=highestqualification,specialisation=specialisation,address=address,password=password1)
            newu.save()
            print('user created!')

            return redirect('/userlogin/')          
        else:

            return redirect('/')   
    else:
        return render(request,"signup.html")


def sent_otp(request):
    if request.method=="POST":
        otp=random.randint(1000,9999)
        email=request.POST.get('email')

        subject='One Last Step!'
        message=f'welcome {email}, \n Your otp is \n{otp}'
        from_email= EMAIL_HOST_USER
        email=request.POST.get('email')     
        send_mail(subject,message,from_email,[email])
        print("sent")

    else:
        return render(request,"verify.html")



def verify(request,email,otp):
    if request.method=="POST":
        totp_device=TOTPDevice.objects.get(email=email,confirmed=True)
    
    else:
        return render(request,"verify.html")




def userlogout(request):
    logout(request)
    return redirect('/')