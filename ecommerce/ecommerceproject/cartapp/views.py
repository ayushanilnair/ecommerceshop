from django.shortcuts import render, redirect, get_object_or_404
from ecommerceapp.models import Product
from .models import Cart,CartItems
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

#impportant
def Addcart(request,product_id):
    product=Product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save(),
    try:
        cart_item=CartItems.objects.get(product=product,cart=cart)
        if cart_item.Quantity < cart_item.product.stock:
            cart_item.Quantity +=1
        cart_item.save()
    except CartItems.DoesNotExist:
        cart_item=CartItems.objects.create(
            product=product,
            Quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('cartapp:Detailcart')

def Detailcart(request,total=0,counter=0,cart_item=None):
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cart_items=CartItems.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            total+=(cart_item.product.price * cart_item.Quantity)
            counter +=cart_item.Quantity

    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))

def cart_remove(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_item=CartItems.objects.get(product=product,cart=cart)
    if cart_item.Quantity > 1:
        cart_item.Quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cartapp:Detailcart')

def full_remove(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_item=CartItems.objects.get(product=product,cart=cart)
    cart_item.delete()
    return redirect('cartapp:Detailcart')