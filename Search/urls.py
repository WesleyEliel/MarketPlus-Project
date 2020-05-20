from django.urls import path, include

from Search import views

urlpatterns = [
    # path('checkout/', views.checkout_view, name='checkout'),
    path('results/', views.results, name='search_results'),
]