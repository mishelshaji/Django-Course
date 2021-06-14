from django.http.response import HttpResponseNotFound
from django.shortcuts import render, HttpResponse, get_object_or_404
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

def list_category(request):
    categories = Category.objects.all()
    context = {}
    context['data'] = categories
    return render(request, 'administrator/category/list.html', context)

def update_category(request, id):
    category = get_object_or_404(Category, id=id)

    if request.method == 'GET':
        context = {}
        context['form'] = CategoryForm(instance=category)
        return render(request, 'administrator/category/update.html', context)
    else:
        form = CategoryForm(data=request.POST, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponse("Data Saved")
        else:
            context = {}
            context['form'] = form
            return render(request, 'administrator/category/update.html', context)