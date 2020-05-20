from django.contrib import admin
from Carts.models import *


# Register your models here.
class CartsAdmin(admin.ModelAdmin):
    pass


class CartItemsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Carts, CartsAdmin)
admin.site.register(CartItems, CartItemsAdmin)
