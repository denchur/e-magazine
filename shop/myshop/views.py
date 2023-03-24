from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from orders.models import Order, OrderItem
from cart.forms import CartAddProductForm
from django.contrib.auth import get_user_model

User = get_user_model()

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'products': products,
    }
    return render(request, 'pages/index.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    pohozhie_prod = Product.objects.filter(category=product.category)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'pohozhie_prod': pohozhie_prod,
        'cart_product_form': cart_product_form
    }
    return render(request, 'pages/product/index.html', context)

def profile(request, username):
    user = get_object_or_404(User, username=username)
    orders = Order.objects.filter(user=user)
    
    context = {
        'user': user,
        'orders': orders,
    }
    return render(request, 'pages/profile/index.html', context)

