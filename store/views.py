from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Category, Product


def all_products(request):
    products = get_list_or_404(Product)
    return render(request, 'store/home.html', {'products': products})


def product_detail(request, slug):
    product_obj = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/product_detail.html', {'product': product_obj})


def category_list(request, category_slug):
    category_obj = get_object_or_404(Category, slug=category_slug)
    product_objs = get_list_or_404(Product, category=category_obj)
    return render(request, 'store/products/category.html', {'category': category_obj, 'product_objs': product_objs})
