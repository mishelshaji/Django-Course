from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'user/home.html')

def about(request):
    return render(request, 'user/about.html')

def contact(request):
    return render(request, 'user/contact.html')

def details(request, id):
    context = {
        'data': id, 
        'message': '<h2>A message from view</h2><script>window.location.href="https://google.com"</script>'
    }
    return render(request, 'user/details.html', context)
