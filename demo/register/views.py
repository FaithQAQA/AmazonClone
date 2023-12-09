from http.client import responses
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages

# Create your views here.


def register_user(request):
    form = SignUpForm()
    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            password= form.cleaned_data['password1']
          

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,("You had made an account"))
            return redirect('home')
        
    return render(request, "register.html", {'form':form})

