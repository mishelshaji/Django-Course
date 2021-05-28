from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    context = {'data': [1, 3, 5, 6]}
    return render(request, 'user/home.html', context)

def about(request):
    return render(request, 'user/about.html')

def contact(request):
    return render(request, 'user/contact.html')

def details(request, id):
    return render(request, 'user/details.html')
