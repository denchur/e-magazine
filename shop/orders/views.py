from django.shortcuts import render, redirect, get_object_or_404
from .models import OrderItem, Status
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    price=cart.get_total_price()
    if request.method == 'POST':
        form = OrderCreateForm(
            request.POST,
            files=request.FILES or None
        )
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.price = price
            order.status = get_object_or_404(Status, pk=1)
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return redirect ('myshop:profile', request.user.username)
    if request.method != 'POST':
        form = OrderCreateForm
    return render(request, 'pages/order/index.html',
                  {'cart': cart, 'form': form})