from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import get_default_password_validators

from django.http import Http404, HttpResponse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.exceptions import * 

# Create your views here.
from django.urls import reverse

from Carts.models import Carts
from .forms import *


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


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def login_view(request):
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
        form = LoginForm()
        page_title = 'M-P | User Login'
    context = locals()
    template = 'registration/login.html'
    return render(request, template, context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            template = 'registration/registration_done.html'
            context = locals()
            return render(request, template, context)
    else:
        form = UserCreationForm()
        page_title = 'User Registration'
    context = locals()
    template = "registration/register.html"
    return render(request, template, context)


@login_required
def userProfile(request):
    user = request.user
    context = locals()
    templates = ''
    return render(request, templates, context)


def my_view(request):
    request_user = request.user
    context = locals()
    template = '404.html'
    return render(request, template, context)

def check_username(request):
    if request.is_ajax():
        is_available = 'false'
        if request.is_ajax():
            username = request.POST.get('username')
            try:
                User.objects.get_by_natural_key(username)
            except ObjectsDoesNotExist:
                is_available = 'true'
        return HttpResponse(is_available)
    raise Http404

def check_email(request):
    if request.is_ajax():
        is_available = 'false'
        if request.is_ajax():
            email = request.POST.get('email')
            try:
                User.objects.get(email=email)
            except ObjectsDoesNotExist:
                is_available = 'true'
        return HttpResponse(is_available)
    raise Http404

def check_password(request):
    if request.is_ajax():
        html = []
        password = request.POST.get('password1')
        if password:
            password_validators = get_default_password_validators()
            for validator in password_validators:
                try:
                    validator.validate(password)
                    response = json.dumps({'success':'True'})
                except ValidationError as error:
                    html.append('<li>'+ error +'</li>')
                    response = json.dumps({'success':'False', 'error':html})
            return HttpResponse(response, content_type='application/javascript; charset=utf-8')
        else:
            raise Http404

def check_re_password(request):
    if request.is_ajax():
        is_available = 'false'
        if request.is_ajax():
            password = request.POST.get('password1')
            re_password = request.POST.get('re_password2')
            if password and re_password and password == re_password:
                is_available = 'true'
            else:
                is_ajax = 'false'
        return HttpResponse(is_available)
    raise Http404
