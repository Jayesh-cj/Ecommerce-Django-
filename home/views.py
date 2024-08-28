from django.shortcuts import render

# Create your views here.

# Home page
def homepage(request):
    return render(request, 'home/homepage.html')