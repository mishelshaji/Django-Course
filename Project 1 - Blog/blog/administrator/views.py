from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.
def create_category(request):
    if request.method == 'GET':
        return render(request, 'administrator/category/create.html')
    elif request.method == 'POST':
        try:
            c = Category()
            c.name = request.POST.get('name')
            c.description = request.POST.get('description')
            c.color = request.POST.get('color')
            c.save()
            return HttpResponse("Data Saved")
        except Exception:
            return HttpResponse("Invalid")