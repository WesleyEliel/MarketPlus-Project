
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from django.urls import path
from Accounts  import views


from .views import *

urlpatterns = [
    path('wes', my_view, name='my_view'),
    path('register/', views.register, name='registration_url'),
    path('login/', views.login_view, name='login_url'),
    path('logout/', views.logout_view, name='logout_url'),

    # reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Ajax requests urls
    path('ajax/check_username/', views.check_username , name='ajax_check_username'),
    path('ajax/check_email/', views.check_email , name='ajax_check_email'),
    path('ajax/check_password/', views.check_password , name='ajax_check_password'),
    path('ajax/check_re_password/', views.check_re_password , name='ajax_check_re_password'),
]

