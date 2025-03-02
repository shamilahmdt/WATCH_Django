from django.shortcuts import render

from watch_web.models import Brand
from watch_web.models import Product
from watch_web.models import Review



def index(request):
    brands = Brand.objects.all()
    products = Product.objects.all()
    reviews = Review.objects.all()

    context = {
        'brands' : brands,
        'products' : products,
        'reviews' : reviews,
    }

    return render(request, 'index.html' , context=context)
