from django.contrib import admin
from .models import *


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    # all the attributes we want to display
    list_display = ['title', 'sale_price', 'active', 'updated']
    # attribute that can be edit
    list_editable = ['sale_price', 'active']
    # filter to help administration search
    list_filter = ['sale_price', 'active']
    # Search field when the administrator try to search
    search_fields = ['title', 'description']
    # Help to display or no the field that can be display
    readonly_fields = ['timestamp', 'updated']
    # Automatic set the slug field base on the title field
    prepopulated_fields = {'slug': ('title',)}


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'thumbnails', 'active', 'featured']
    list_editable = ['thumbnails', 'active', 'featured']


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'user', 'date', 'rating', 'is_approved')
    list_per_page = 20
    list_filter = ('product', 'user', 'is_approved')
    ordering = ['date']
    search_fields = ['user','content','title']

class ProductAnonymousReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'complete_name', 'email', 'date', 'rating', 'is_approved')
    list_per_page = 20
    list_filter = ('product', 'complete_name', 'is_approved')
    ordering = ['date']
    search_fields = ['complete','content','title']


@admin.register(DealOfTheWeek)
class DealOfTheWeekAdmin(admin.ModelAdmin):
    # all the attributes we want to display
    list_display = ['title', 'sale_price', 'active', 'updated', 'valid_from', 'valid_to']
    # attribute that can be edit
    list_editable = ['sale_price', 'active', 'valid_from', 'valid_to']
    # filter to help administration search
    list_filter = ['sale_price', 'active','valid_from', 'valid_to']
    # Search field when the administrator try to search
    search_fields = ['title', 'description']
    # Help to display or no the field that can be display
    readonly_fields = ['timestamp', 'updated']
    # Automatic set the slug field base on the title field
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(ProductImage, ProductImageAdmin)
# admin.site.register(Review)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(ProductAnonymousReview, ProductAnonymousReviewAdmin)
