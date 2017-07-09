# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import FoodPermitForm
from django.shortcuts import redirect
from .models import FoodPermit
from .filters import FoodPermitFilter
from django.http import HttpResponse
import populate_script
import find_nearest

#from .tasks import auto_expire

def index(request):
	context = {}
	return render(request, 'index.html', context)

def search(request):
	foodpermit_list = FoodPermit.objects.all()
	foodpermit_filter = FoodPermitFilter(request.GET, queryset=foodpermit_list)

	return render(request, 'search.html', {'filter': foodpermit_filter})


def add_entry(request):
	if request.method == 'POST':
		form = FoodPermitForm(request.POST)
		if form.is_valid():
			foodpermit = form.save(commit=False)
			newform = FoodPermitForm()
			foodpermit.save()
	
	form = FoodPermitForm() 
	return render(request, 'add_entry.html', {'form':form})

def predict_best(request):
	if request.method == 'POST':
		ans = find_nearest.get_truck_name(request.POST.get('locationid'))
		ans = "Best truck for searched location id : " + str(ans)
		return render(request, 'predict_best.html', {'ans': ans})
	
	context = {'ans' : ''}
	return render(request, 'predict_best.html', context)

def populate(request):
	k, flag = populate_script.populate()
	return HttpResponse("Populating " + str(k) + " Done exceptions " + str(flag))

def delete_entry(request, locationid=None):
	if request.method == 'POST':
		FoodPermit.objects.filter(locationid=locationid).delete()
	return search(request)

def auto_update(request):
#	auto_expire(repeat = 86400)
	return HttpResponse("auto_expire called :)")