from django.shortcuts import get_object_or_404

from Carts.models import Carts, CartItems


def get_cart_items(request):
    try:
        the_id = request.session['cart_id']
    except KeyError:
        the_id = None
    if the_id:
        cart = Carts.objects.get(session_id=the_id)
        cart_items = cart.cartitems_set.all()
        return cart_items
    else:
        return None


def cart_distinct_item_count(request):
    try:
        session_id = request.session['cart_id']
        cart = Carts.objects.get(session_id=session_id)
        count = cart.cartitems_set.all().count()
    except:
        pass
    return count


def get_single_item(request, item_id):
    try:
        session_id = request.session['cart_id']
        cart = Carts.objects.get(session_id=session_id)
        cart_item = CartItems.objects.get(cart=cart, id=item_id)
        return cart_item
    except:
        return None


def is_empty(request):
    try:
        session_id = request.session['cart_id']
        cart = Carts.objects.get(session_id=session_id)
        return cart.cartitems_set.all().count() == 0
    except:
        pass



def empty_cart(request):
    try:
        session_id = request.session['cart_id']
        cart = Carts.objects.get(session_id=session_id)
    except:
        pass
    for items in cart.cartitems_set.all():
        items.delete()
