"""MarketPlus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# Loading urls to include in this globals URLs
import Accounts.urls as AccountsUrls
import Blog.urls as BlogUrls
import Marketing.urls as MarketingUrls
import Orders.urls as OrdersUrls
import Products.urls as ProductsUrls
import Search.urls as SearchUrls

# Loading views to match other URLs
from Products import views as products_views
from Carts import views as carts_views
from Search import views as search_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # My own paths
    path('', products_views.home, name='home'),
    # path('', products_views.base_view, name='base_view'),


    # Including my applications's paths
    path('accounts/', include(AccountsUrls)),
    path('accounts_wes/', include('django.contrib.auth.urls')),
    path('blog/', include(BlogUrls)),
    path('marketing/', include(MarketingUrls)),
    path('orders/', include(OrdersUrls)),
    path('products/', include(ProductsUrls)),
    path('search/', include(SearchUrls)),
    # Managing cart url in the global URLs
    path('cart/', carts_views.view, name='cart_view'),
    path('add_to_cart/<slug:slug>', carts_views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug:slug>', carts_views.add_to_cart, name='remove_from_cart'),
    path('clear_cart/', carts_views.clear_cart, name='cart_clear'),
    path('update_cart/', carts_views.update_cart, name='update_cart'),
    path('base', carts_views.base, name='base'),

    # Managing cart url in the global URLs
    path('search/', search_views.results, name='search_results'),

    # path('accounts/', include('allauth.urls')),
    path('social-auth/', include('social_django.urls',	namespace='social')),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
