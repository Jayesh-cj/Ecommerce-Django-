from django.shortcuts import render

from products.models import Product

# Create your views here.

# Home page
def homepage(request):
    context = {'products' : Product.objects.all() }
    return render(request, 'home/homepage.html', context)

