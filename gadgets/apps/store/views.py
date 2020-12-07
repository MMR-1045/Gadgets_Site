from django.shortcuts import render

from .models import Product,Category
# Create your views here.

def product_detail(request,category_slug, slug):
    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product,
        # 'imagesstring': imagesstring,
        # 'related_products': related_products
    }

    return render(request, 'product_detail.html', context)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()

    context = {
        'category': category,
        'products': products,
    }

    return render(request, 'category_detail.html', context)