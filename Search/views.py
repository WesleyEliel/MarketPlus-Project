from django.shortcuts import render
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from Carts.models import Carts, CartItems
from MarketPlus import settings
from Search import search


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


def results(request):
    # get current search phrase
    q = request.GET.get('q', '')
    # get current page number. Set to 1 is missing or invalid
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1
    # retrieve the matching products
    matching = search.products(q).get('products')
    # generate the paginator object
    paginator = Paginator(matching, settings.PRODUCTS_PER_PAGE)
    try:
        results = paginator.page(page).object_list
    except (InvalidPage, EmptyPage):
        results = paginator.page(1).object_list
        # store the search
    search.store(request, q)
    # the usual…
    page_title = 'Search Results for: ' + q

    template_name="products/products_search.html"
    context = locals()
    return render(request, template_name, context)
