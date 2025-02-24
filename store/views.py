from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Mobile, Cart

def cart_view(request):
    cart_id = request.session.get('cart_id')
    if not cart_id:
        # If cart_id is not present in the session, create a new cart and set the session key
        cart = Cart.objects.create(user=request.user.username)
        request.session['cart_id'] = cart.id
    else:
        try:
            cart = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            return HttpResponse("Cart not found", status=404)

    mobile_id = request.GET.get('mobile_id')
    if mobile_id:
        item = cart.get_item(mobile_id)
        return render(request, 'cart.html', {'item': item})
    else:
        return render(request, 'cart.html', {'item': None})

def index(request):
    mobiles = Mobile.objects.all()
    return render(request, 'index.html', {'mobiles': mobiles})

def home(request):
    mobiles = Mobile.objects.all()
    return render(request, 'home.html', {'mobiles': mobiles})

def add_to_cart(request, mobile_id):
    mobile = get_object_or_404(Mobile, id=mobile_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user.username, mobile=mobile)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')
