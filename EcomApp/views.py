from django.shortcuts import render,get_object_or_404
from .models import Product

# Create your views here.

def product_list(request):
    data = Product.objects.all()
    return render(request,'ProductList.html',{'data':data})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'ProductDetail.html', {'product': product})


