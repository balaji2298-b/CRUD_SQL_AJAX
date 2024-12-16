from django.shortcuts import render,redirect
from myapp.models import Batmen



def index(request):
	batmens = Batmen.objects.all()
	context = {'batmens':batmens}
	return render(request,'index.html',context)

def create(request):
	batmen = Batmen(name=request.POST.get('name'),mobilenumber= request.POST.get('mobilenumber'),age=request.POST.get('age'),city=request.POST.get('city'))
	batmen.save()
	return redirect('/')

def read(request):
	return render(request,'index.html')

def edit(request,id):
	batmen = Batmen.objects.get(id=id)
	context = {'batmen':batmen}
	return render(request,'edit.html',context)

def update(request,id):
	batmen = Batmen.objects.get(id=id)
	batmen.name = request.POST.get('name')
	batmen.mobilenumber = request.POST.get('mobilenumber')
	batmen.age = request.POST.get('age')
	batmen.city = request.POST.get('city')
	batmen.save()
	return redirect('/')
	
	
def delete(request,id):
	batmen = Batmen.objects.filter(id=id)
	batmen.delete()
	return redirect('/')
