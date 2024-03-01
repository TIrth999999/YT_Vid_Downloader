from django.shortcuts import render, redirect
from django.contrib.auth.models import User,AnonymousUser
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from pytube import YouTube
import sys

def index(request):
     return render(request,'index.html')

def loginUser(request):
    
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        if user is not None:
            messages.success(request, 'Congratulations for logging in :)')
            login(request, user)
            return redirect('index')
        else:
            return render( request,'login.html')
        
    return render(request,'login.html')

def signupUser(request):
    
    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')   

        if(pass1 != pass2):
            messages.error(request, 'Password did not matched')
            return redirect('signup')
        
        Myuser = User.objects.create_user(username, email, pass1)
        Myuser.save()
        messages.success(request, 'Congratulations for Creating new Account :)')

        return redirect('login')

    return render(request,'signup.html')

def contact(request):
            if request.user.is_anonymous:
                return redirect('login')
            return render(request,'contact.html')
            
def service(request):
        if request.user.is_anonymous:
            return redirect('login')
        
        if request.user.is_active == False:
            return redirect('login')

        if request.user.is_active:
            
            if request.method == 'POST':
                link = request.POST.get('abc')
                yt = YouTube(link)
                x = yt.streams.get_highest_resolution()
                x.download(request.POST.get('path'))
                print("Download completed")
            else:
                print("No URL provided")

        return render(request,'service.html')

def logoutUser(request):
     logout(request)
     messages.success(request, 'Congratulations for logging out :)')
     return redirect('login')