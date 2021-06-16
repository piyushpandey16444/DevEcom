from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Product, Category
from django.contrib.auth.models import User


def all_products(request):
    products = get_list_or_404(Product)
    return render(request, 'store/home.html', {'products': products})


def product_detail(request, slug):
    product_obj = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'product/product_detail.html', {'product': product_obj})
