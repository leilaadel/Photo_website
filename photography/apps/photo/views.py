from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'photo/index.html')

def about(request):
    return render(request, 'photo/about.html')

def gallery(request):
    return render(request, 'photo/gallery.html')

def contact(request):
    return render(request, 'photo/contact.html')
