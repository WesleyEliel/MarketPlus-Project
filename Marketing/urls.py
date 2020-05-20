
from django.contrib import admin
from django.urls import path, include
import Marketing.views as marketing_views

urlpatterns = [
    path('about', marketing_views.about_view, name='about_view'),
    path('contact', marketing_views.contact_view, name='contact_view'),

    # path(r'^robots\.txt$', 'robots'),

]