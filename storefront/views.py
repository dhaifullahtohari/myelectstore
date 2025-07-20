from django.shortcuts import render
from catalog.models import Product

def home(request):
    products = Product.objects.filter(is_active=True).order_by('-created_at')[:8]  # أحدث 8 منتجات
    return render(request, 'home.html', {'products': products})
