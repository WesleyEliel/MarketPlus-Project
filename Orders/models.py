import decimal

from django.contrib.auth import get_user_model
from django.db import models
from Carts.models import *

# Create your models here.

User = get_user_model()

CHOICES = (
    ("submitted", "Submitted"),
    ("started", "Started"),
    ("abandoned", "Abandoned"),
    ("finished", "Finished"),
)


class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    order_id = models.CharField(max_length=120, unique=True)
    transaction_id = models.CharField(max_length=120, unique=True)
    cart = models.ForeignKey(Carts, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=120, choices=CHOICES, default='submitted')
    ip_address = models.GenericIPAddressField(null=True)
    sub_total = models.DecimalField(max_digits=100, decimal_places=2)
    tax_total = models.DecimalField(max_digits=100, decimal_places=2)
    final_total = models.DecimalField(max_digits=100, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    # contact info
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    #Billing informations
    billing_first_name = models.CharField(max_length=50, null=True)
    billing_last_name = models.CharField(max_length=50, null=True)
    billing_address_1 = models.CharField(max_length=50, null=True)
    billing_address_2 = models.CharField(max_length=50, blank=True, null=True)
    billing_city = models.CharField(max_length=50, null=True)
    billing_state = models.CharField(max_length=2, null=True)
    billing_country = models.CharField(max_length=50, null=True)
    billing_zip = models.CharField(max_length=10, null=True)
    billing_other_note = models.TextField(null=True)
    # other
    shipping_different_address = models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.order_id)

    @property
    def total(self):
        total = decimal.Decimal('0.00')
        order_items = OrderItem.objects.filter(order=self)
        for item in order_items:
            total += item.total
        return total


class ShippingAddress(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # shipping information
    shipping_first_name = models.CharField(max_length=50,  null=True)
    shipping_last_name = models.CharField(max_length=50,  null=True)
    shipping_address_1 = models.CharField(max_length=50, null=True)
    shipping_address_2 = models.CharField(max_length=50, blank=True, null=True)
    shipping_city = models.CharField(max_length=50, null=True)
    shipping_state = models.CharField(max_length=2, null=True)
    shipping_country = models.CharField(max_length=50, null=True)
    shipping_zip = models.CharField(max_length=10, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    @property
    def total(self):
        return self.quantity * self.price
