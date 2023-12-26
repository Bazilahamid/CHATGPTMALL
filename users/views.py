from django.shortcuts import render

# Create your views here.

def HomePage(request):
    return render (request, 'homepage.html')

def LoginView(request):
    return render (request, 'login.html')

def RegisterView(request):
    return render (request, 'register.html')

#def HomePage(request):
 #def HomePage(request):