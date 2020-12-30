from django.shortcuts import render,redirect
from lab_covid.models import Login
from django.http import HttpResponse
from lab_covid.forms import Loginform
# Create your views here.
def login(request):
	if request.method=="POST":
	       username=request.POST['username']
	       password=request.POST['password']
	       data=Login.objects.create(username=username,password=password)
	       return redirect('home')
	return render(request,"lab_covid/login.html") 

def lab1(request):
	return render(request,'lab_covid/lab1.html')

def home(request):
	return render(request,'lab_covid/home.html')