from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from accounts.models import *
from accounts.forms import *
from django.http import *
from .filters import SnippetFliter
from django.db.models import Q
from .models import clientdetails
from django.contrib.auth.models import User
from travello.models import Destination
from .forms import client_form




# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
        
            return redirect( '/')

        else:
            messages.error(request, ' invalid creddentils')
            return redirect('/')

    else:
        messages.warning(request, 'Somethings went wrong, contact us')
        return redirect('/')






def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']





        if password1 == password2 :
            
            if User.objects.filter(username = username).exists():
                messages.warning(request, 'username exists')
                return redirect(request, 'users')
            elif User.objects.filter(email = email).exists():
                messages.warning(request, 'email exists')
                return render(request, 'users')
        
            else:
                user = User.objects.create_user(username = username, password = password1, email = email, first_name = first_name )
                user.save()
                messages.success(request, 'register successful, login to start journy with us')
                return redirect('/')
                print('user created')

        else:

            messages.warning(request, 'password does not match')
            return render(request, 'users')
        
    else:
        messages.warning(request, 'something went wrong, contact us')
        return redirect( '/')


def logout(request):
    auth.logout(request)
    messages.info(request, 'you logout')
    return redirect('/')



def users(request):
    return render(request, 'loginsignup.html')


def destination_click(request, city):

    if request.user.is_authenticated:

        return render(request,'booktrip.html', {'city':city}) 
       
    else: 
        messages.info(request, 'login first!')
        return render(request, '/')






def clientdetails1(request, city_name):

    
    if request.method == 'POST':
        
        form=client_form(request.POST)
        print(form.errors)
        if form.is_valid():  
           
            instance = form.save(commit=False)
            instance.owner=request.user


            var2=Destination.objects.filter(name=city_name)

            for varr in var2:
                var_1={ varr.price }
                var__1=var_1
                var_2={ varr.dec }
                var__2=var_2
                var_3={ varr.agentnumber }
                var__3=var_3
                var_4={ varr.agent_address }
                var__4=var_4
                var_5={ varr.image }
                var__5=var_5

            for var___1 in var__1:
                var____1=var___1

            for var___2 in var__2:
                var____2=var___2

            for var___3 in var__3:
                var____3=var___3

            for var___4 in var__4:
                var____4=var___4

            for var___5 in var__5:
                var____5=var___5

            




            instance.price=var____1
            instance.dec=var____2
            instance.agentnumber=var____3
            instance.agent_address=var____4
            instance.image=var____5







            instance.save()
            messages.success(request, 'congrulation, trip book')
            print(messages)
            print('v')
            return redirect('/')
        messages.info(request, 'enter valid data, somethong went wrong')
        print(messages)
        print('v')
        return redirect('/')
    else:
        messages.warning(request, 'something went wrong, contact us')
        return redirect('/')



def yourtrips(request):

   
    query1 =  clientdetails.objects.filter(owner=request.user)

    
    

    return render(request, 'yourtrips.html',{'dests':query1}) 



def More_Details(request, client_id):

    shows = clientdetails.objects.filter(id=client_id)

    return render(request, 'More_Details.html', {'shows':shows})




