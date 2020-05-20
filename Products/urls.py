
from django.contrib import admin
from django.urls import path

from Products import views

urlpatterns = [
    path('', views.products_view, name='shop'),
    path('<slug:slug>', views.single_product_view, name='product_single'),
    path('<slug:slug>', views.product_category_view, name=''),
    path('<slug:slug>', views.search_product_by_category_view, name=''),
    path('review/add/', views.add_review, name='review_add'),
    path('anonymous_review/add/', views.add_anonymous_review, name='anonymous_review_add'),

]