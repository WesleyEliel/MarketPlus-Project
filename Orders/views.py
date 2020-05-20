import time

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse

from django.template import RequestContext
from django.http import HttpResponseRedirect
from Orders.forms import CheckoutForm
from Orders.models import Order, OrderItem
from Orders import checkout
from Carts import cart

from Orders.forms import *
from Orders.models import *
from Carts.models import *
from Accounts.forms import *
from .utils import id_generator


def show_cart_in_panel(request):
    try:
        the_id = request.session['cart_id']
    except KeyError:
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
    return empty, cart


# Create your views here.


def order(request):
    template = 'orders/users.html'
    context = locals()


def show_checkout(request):
    if cart.is_empty(request):
        cart_url = reverse('show_cart')
        return HttpResponseRedirect(cart_url)
    if request.method == 'POST':
        post_data = request.POST.copy()
        form = CheckoutForm(post_data)
        if form.is_valid():
            request.session['coupon_code'] = form.clean_data['coupon_code']
            response = checkout.process(request)
            order_number = response.get('order_number', 0)
            error_message = response.get('message', '')
            if order_number:
                request.session['order_number'] = order_number
                receipt_url = reverse('checkout_receipt')
                return HttpResponseRedirect(receipt_url)
        else:
            error_message = 'Correct the errors below'
    else:
        form = CheckoutForm()

    page_title = 'Checkout'
    context = locals()
    template = 'orders/checkout.html'
    return render(request, template, locals())


def receipt(request):
    order_number = request.session.get('order_number', '')
    if order_number:
        order = Order.objects.filter(id=order_number)[0]
        order_items = OrderItem.objects.filter(order=order)
        del request.session['order_number']
    else:
        cart_url = reverse('cart_view')
        return HttpResponseRedirect(cart_url)

    context = locals()
    template = 'orders/receipt.html'
    return render(request, template, context)


def checkout_view(request):
    try:
        the_id = request.session['cart_id']
        cart = Carts.objects.get(id=the_id)
    except KeyError:
        the_id = None
        return HttpResponseRedirect(reverse('cart_view'))
    try:
        new_order = Order.objects.get(cart)
    except Order.DoesNotExist:
        new_order = Order()
        new_order.cart = cart
        new_order.user = request.user
        new_order.order_id = id_generator()
        new_order.save()
    except:
        return HttpResponseRedirect(reverse('cart_view'))

    if new_order.status == "Finished":
        cart.delete()
        del request.session['items_total']
        del request.session['cart_id']
        HttpResponseRedirect(reverse('cart_view'))

    context = locals()
    template = 'index.html'
    return render(request, template, context)

def user_identification(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if	form.is_valid():
            cd	=	form.cleaned_data
            user	=	authenticate(request, username=cd['username'], password=cd['password'])
            if	user	is	not	None:
                if	user.is_active:
                    login(request,	user)
                    return	HttpResponse('Authenticated	Successfully')
                else:
                    return	HttpResponse('Disabled account')
            else:
                return	HttpResponse('Invalid login')
    else:
        login_form = LoginForm()
        register_form = UserCreationForm()
        page_title = 'M-P|User Identification'
    context = locals()
    template = 'orders/identification.html'
    return render(request, template, context)


def ajax_check_email():
    pass

def ajax_check_paycard():
    pass

def ajax_check_billing_part():
    pass

def ajax_check_shipping_part():
    pass

def ajax_checkout_identification():
    pass