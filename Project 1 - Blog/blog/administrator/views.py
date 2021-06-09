from django.shortcuts import render, HttpResponse
from .models import *
from .forms import *

# Create your views here.
def create_category(request):
    if request.method == 'GET':
        context = {}
        context['form'] = CategoryForm()
        return render(request, 'administrator/category/create.html', context)

    elif request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Data Saved")
        else:
            context = {}
            context['form'] = form
            return render(request, 'administrator/category/create.html', context)