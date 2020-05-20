from django.shortcuts import render

from Carts.models import Carts , CartItems


def show_cart_in_panel(request):
    try:
        the_id = request.session['cart_id']
    except KeyError:
        the_id = None
    empty = None
    cart = None
    if the_id:
        try:
            cart = Carts.objects.get(session_id=the_id)
            request.session['total_items'] = cart.cartitems_set.count()
            empty = False
        except Carts.DoesNotExist:
            if request.session['total_items']:
                del request.session['total_items']
            empty = True
    else:
        empty = True
        cart = None
    return empty, cart


# Create your views here.
