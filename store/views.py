from django.shortcuts import render, get_list_or_404
from .models import Product, Category
from django.contrib.auth.models import User


def all_products(request):
    products = get_list_or_404(Product)
    return render(request, 'store/home.html', {'products': products})
