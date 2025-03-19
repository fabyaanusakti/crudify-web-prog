from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def test(request):
    return render(request, 'test.html')

def register(request):
    return render(request, 'register.html')