from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from minip.forms import RegisterForm,IndexForm
from django.http import HttpResponse
from minip.models import Index
from django.contrib.auth.models import User

# Create your views here.
def signin(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user = authenticate(request,username=username,password=password)
		print(user)
		if user is not None:
			login(request,user)
			return redirect('/home')
		else:
			return HttpResponse("Success")
	return render(request,'minip/signin.html')

def register(request):
	form=RegisterForm()
	if request.method=='POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			user=form.cleaned_data.get('email')
			print(user)
			return redirect('/signin')
	return render(request, 'minip/register.html', {'form': form})

def home(request):
	return render(request,"minip/home.html")

def index(request):
	if request.method=="POST":
		f_name=request.POST['f_name']
		l_name=request.POST['l_name']
		phonenumber=request.POST['phonenumber']
		rollnumber=request.POST['rollnumber']
		reservationdate=request.POST['reservationdate']
		emailid=request.POST['emailid']
		lab=request.POST['lab']
		session=request.POST['session']
		hint=Index(f_name=f_name,l_name=l_name,phonenumber=phonenumber,rollnumber=rollnumber,reservationdate=reservationdate,emailid=emailid,lab=lab,session=session)
		hint.save()
		return redirect('/home')
	return render(request,"minip/index.html")
