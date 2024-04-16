from django.shortcuts import render

from main.models import Products


def index(request):
    products = Products.objects.all()

    context = {
        'title': 'Assemble Your Team',
        'products': products
    }

    return render(request, 'main/index.html', context)

def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        'title': product.name,
        "product": product
    }

    return render(request, "main/product.html", context=context)
