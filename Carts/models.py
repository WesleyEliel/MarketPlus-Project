from django.db import models
from Products.models import Product
from xml.dom.minidom import Document
from Coupons.models import *


# Create your models here.

class Carts(models.Model):
    session_id = models.CharField(max_length=120)
    coupon_id = models.CharField(max_length=250, null=True, blank=True)
    total = models.DecimalField(decimal_places=2, max_digits=100, default=00.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str("Id:{}, Session Id : {}".format(self.id, self.session_id))
    
    @property
    def coupon(self):
        if self.coupon_id and self.coupon_id != 'null':
            return Coupon.objects.get(id=self.coupon_id)
        return None
    
    
    def get_total_price(self):
        return self.total


    def get_discount(self):
        if self.coupon:
            return (self.coupon.discount / Decimal('100'))* self.get_total_price()
        return Decimal('0')

    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()


class CartItems(models.Model):
    cart = models.ForeignKey(Carts, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, default=0)
    line_total = models.DecimalField(decimal_places=2, max_digits=100, default=00.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str('Cart n° {}, Cart Items n°{}'.format(self.cart.id, self.id))

    @property
    def description(self):
        if self.product.sale_price > self.product.normal_price:
            return self.product.sale_price
        else:
            return self.product.normal_price

    @property
    def name(self):
        return str("Cart Session N°{}; Cart Item of {}".format(self.cart.session_id, self.product.title))

    @property
    def price(self):
        if self.product.sale_price > self.product.normal_price:
            return self.product.sale_price
        else:
            return self.product.normal_price
