from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render
from django.template.loader import render_to_string
import json as simplejson
from django.http import HttpResponse
from django.utils import timezone
import random
from MarketPlus.settings import PRODUCTS_PER_ROW
from Stats import stats
from .models import Product
from .forms import *
from .utils import *
from Blog.models import *
from Carts.models import *

# Create your views here.


def home(request):
    all_products_list = []
    products_list = Product.objects.all()
    
    # Others queryset
    search_recs = stats.recommended_from_search(request)
    recently_viewed = stats.get_recently_viewed(request)
    view_recs = stats.recommended_from_views(request)

    # products to render list
    all_products_list += products_list

    if search_recs != None:
        all_products_list += search_recs

    if view_recs != None:
        all_products_list += view_recs

    random.shuffle(all_products_list)
    if recently_viewed != None:
        all_products_list = list(recently_viewed[:4]) + all_products_list
    all_products_list = remove_duplicate(all_products_list)
    print(all_products_list)
    print('\n')
    print(len(all_products_list))
    all_products_list = list_to_queryset(Product, all_products_list)
    print('\n\n\n')
    print(all_products_list)
    print('\n')
    print(len(all_products_list))

    paginator = Paginator(all_products_list, 16)
    page = request.GET.get('page')
    # Deal of this week
    now = timezone.now()
    deal_of_this_week = DealOfTheWeek.objects.filter(valid_from__lte=now, valid_to__gte=now, active=True).order_by('updated')[0]
    
    blog_post = Post.objects.order_by('publish')[:3]
    all_products = paginator.get_page(page)
    empty, cart = show_cart_in_panel(request)
    template = 'index.html'
    context = locals()
    return render(request, template, context)


def products_view(request):
    new_products = Product.objects.order_by('updated')
    best_sells = Product.objects.all()
    most_populars = Product.objects.order_by('-views')
    catalogue_list_query = Product.objects.all()
    catalogue_list = []
    catalogue_list += catalogue_list_query
    random.shuffle(catalogue_list)
    paginator = Paginator(catalogue_list, 16)
    page = request.GET.get('page')

    catalogue = paginator.get_page(page)

    # Others queryset
    search_recs = stats.recommended_from_search(request)
    featured = Product.is_featured.all()[0:PRODUCTS_PER_ROW]
    recently_viewed = stats.get_recently_viewed(request)
    view_recs = stats.recommended_from_views(request)

    # Deal of the week code
    now = timezone.now()
    deal_of_this_week = DealOfTheWeek.objects.filter(valid_from__lte=now, valid_to__gte=now, active=True).order_by('updated')[0]
    dow_delta_time = deal_of_this_week.valid_to - deal_of_this_week.valid_from
    #dow_days, dow_hours, dow_minutes, dow_secondes = dow_delta_time.days, dow_delta_time.seconds//3600, dow_delta_time.seconds%3600//60, (dow_delta_time.seconds%3600)%60
    dow_year = deal_of_this_week.valid_to.year
    dow_month = deal_of_this_week.valid_to.month
    dow_day = deal_of_this_week.valid_to.day
    dow_hour = deal_of_this_week.valid_to.hour
    dow_minute = deal_of_this_week.valid_to.minute
    dow_seconde = deal_of_this_week.valid_to.second
    print(now)
    print(deal_of_this_week)
    empty, cart = show_cart_in_panel(request)
    template = 'products/products.html'
    context = locals()
    return render(request, template, context)


def product_category_view(request):
    # Others queryset
    search_recs = stats.recommended_from_search(request)
    featured = Product.featured.all()[0:PRODUCTS_PER_ROW]
    recently_viewed = stats.get_recently_viewed(request)
    view_recs = stats.recommended_from_views(request)


def search_product_by_category_view(request):
    # Others queryset
    search_recs = stats.recommended_from_search(request)
    featured = Product.featured.all()[0:PRODUCTS_PER_ROW]
    recently_viewed = stats.get_recently_viewed(request)
    view_recs = stats.recommended_from_views(request)


def single_product_view(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        product.views += 1
        product.save()
    except Product.DoesNotExist:
        raise Http404("This products does not exists, please back to shopping ")
    
    #Search terms by category
    search_category_by_name = product.category.name
    search_category_by_color = product.category.product_color
    search_category_by_theme_color = product.category.product_theme_color

    # Others queryset
    search_recs = stats.recommended_from_search(request)
    recently_viewed = stats.get_recently_viewed(request)
    view_recs = stats.recommended_from_views(request)

    related_products = []
    related_products += Product.objects.filter(category__name__contains=search_category_by_name)
    related_products += Product.objects.filter(category__product_color__contains=search_category_by_color)
    related_products += Product.objects.filter(category__product_color__contains=search_category_by_theme_color)
    related_products += Product.objects.filter(category__product_theme_color__contains=search_category_by_color)
    related_products += Product.objects.filter(category__product_theme_color__contains=search_category_by_theme_color)
    if search_recs != None:
        related_products += search_recs
    if recently_viewed != None:
        related_products += recently_viewed
    if view_recs != None:
        related_products += view_recs
    random.shuffle(related_products)
    related_products = remove_duplicate(related_products)
    related_products = list_to_queryset(Product, related_products)

    # Reviews on single
    product_reviews = []
    reviews = ProductReview.approved.filter(product=product).order_by('-date')[:5]
    anonymous_reviews = ProductAnonymousReview.approved.filter(product=product).order_by('-date')[:5]
    product_reviews += reviews
    product_reviews += anonymous_reviews 
    reviews_number = int(ProductReview.approved.filter(product=product).count() + ProductAnonymousReview.approved.filter(product=product).count())
    review_form = ProductReviewForm()
    anonymous_review_form = ProductAnonymousReviewForm()

    empty, cart = show_cart_in_panel(request)
    template = 'products/product_single.html'
    context = locals()
    return render(request, template, context)


def add_review(request):
    form = ProductReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        slug = request.POST.get('slug')
        rating = request.POST.get('rating')
        product = Product.active.get(slug=slug)
        review.user = request.user
        review.product = product
        review.save()
        template = "products/product_review.html"
        html = render_to_string(template, {'review': review })
        response = simplejson.dumps({'success':'True', 'html': html})
    else:
        html = form.errors.as_ul()
        response = simplejson.dumps({'success':'False', 'html': html})
    return HttpResponse(response, content_type='application/javascript; charset=utf-8')


def add_anonymous_review(request):
    form = ProductAnonymousReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        slug = request.POST.get('slug')
        rating = request.POST.get('rating')
        product = Product.active.get(slug=slug)
        review.product = product
        review.rating = rating
        review.save()
        template = "products/product_review.html"
        html = render_to_string(template, {'review': review })
        response = simplejson.dumps({'success':'True', 'html': html})
    else:
        html = form.errors.as_ul()
        response = simplejson.dumps({'success':'False', 'html': html})
    return HttpResponse(response, content_type='application/javascript; charset=utf-8')
