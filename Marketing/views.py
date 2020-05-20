from django.shortcuts import render
from Carts.models import *
from django.http import HttpResponse
from MarketPlus.settings import CURRENT_PATH
import os


# Create your views here.

def show_cart_in_panel(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None
    empty = None
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


ROBOTS_PATH = os.path.join(CURRENT_PATH, 'marketing/robots.txt')


def robots(request):
    return HttpResponse(open(ROBOTS_PATH).read(), 'text/plain')


def contact_view(request):
    empty, cart = show_cart_in_panel(request)
    template = 'others/contact.html'
    context = locals()
    return render(request, template, context)


def about_view(request):
    empty, cart = show_cart_in_panel(request)
    template = 'others/about.html'
    context = locals()
    return render(request, template, context)
