import random

from django.core import serializers
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from Carts.cart import get_single_item
from Carts.models import *
from Products.models import *
from Stats import stats


# Create your views here.


def _generate_cart_id():
    cart_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRQSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    cart_id_length = 50
    for y in range(cart_id_length):
        cart_id += characters[random.randint(0, len(characters) - 1)]
    return cart_id


def view(request):
    try:
        the_id = request.session['cart_id']
    except KeyError:
        the_id = None

    # the_id = 6
    if the_id:
        try:
            cart = Carts.objects.get(session_id=the_id)
            request.session['total_items'] = cart.cartitems_set.count()
            empty = False
            context = {'cart': cart, }
        except Carts.DoesNotExist:
            if request.session['total_items']:
                del request.session['total_items']
            empty = True
            context = {'empty': empty}
    else:
        empty = True
        context = {'empty': empty}

    # Others queryset
    search_recs = stats.recommended_from_search(request)
    recently_viewed = stats.get_recently_viewed(request)
    view_recs = stats.recommended_from_views(request)
    context['search_recs'] = search_recs
    context['recently_viewed'] = recently_viewed
    context['view_recs'] = view_recs

    template = 'carts/carts.html'
    return render(request, template, context)


def add_to_cart(request, slug):
    try:
        the_id = request.session['cart_id']
    except:
        cart = Carts()
        session_id = str(_generate_cart_id())
        cart.session_id = session_id
        cart.save()
        request.session['cart_id'] = cart.session_id
        the_id = cart.session_id
    try:
        cart = Carts.objects.get(session_id=the_id)
    except:
        del request.session['cart_id']
        return HttpResponseRedirect(reverse('cart_view'))

    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        print('The product is not register')
    except:
        pass

    cart_item, created = CartItems.objects.get_or_create(cart=cart, product=product)
    try:
        qty = request.GET.get('qty')
    except KeyError:
        print('No QTY attribute founded in request session')
    except:
        pass

    if qty == None:
        qty = 0

    if created:
        if int(qty) == 0:
            qty = 1
        cart_item.quantity = int(qty)
        cart_item.save()
    else:
        if int(qty) == 0:
            cart_item.delete()
        else:
            cart_item.quantity += int(qty)
            cart_item.save()

    new_total = 0.00
    for items in cart.cartitems_set.all():
        line_total = float(items.product.sale_price) * items.quantity
        items.line_total = line_total
        new_total += line_total
        items.save()

    request.session['total_items'] = cart.cartitems_set.count()
    cart.total = new_total
    cart.save()

    # Others queryset
    search_recs = stats.recommended_from_search(request)
    recently_viewed = stats.get_recently_viewed(request)
    view_recs = stats.recommended_from_views(request)

    template = 'carts/carts.html'
    context = locals()
    return render(request, template, context)


def remove_from_cart(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        item = CartItems.objects.get(product=product)
    except:
        return HttpResponseRedirect(reverse('cart_view'))
    item.delete()
    return HttpResponseRedirect(reverse('cart_view'))


def update_cart(request):
    post_data = request.POST.copy()
    item_id = post_data['item_id']
    quantity = request.GET.get('qty')
    cart_item = get_single_item(request, item_id)
    if cart_item:
        if int(quantity) > 0:
            cart_item.quantity = int(quantity)
            cart_item.save()
            return HttpResponseRedirect(reverse('cart_view'))
        else:
            product_slug = cart_item.product.slug
            remove_from_cart(request, product_slug)
    else:
        return HttpResponseRedirect(reverse('cart_view'))


def clear_cart(request):
    pass


def base(request):
    return render(request, 'base.html', locals())
