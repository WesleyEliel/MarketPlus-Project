
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    # path('checkout/', views.checkout_view, name='checkout'),
    path('checkout/', views.show_checkout, name='checkout'),
    path('receipt/', views.receipt, name='receipt'),
    path('user_identification/', views.user_identification, name='checkout_identification')

]