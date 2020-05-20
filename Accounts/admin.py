from django.contrib import admin
from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    # all the attributes we want to display
    list_display = ['username', 'first_name', 'last_name', 'email', 'phone']
    # attribute that can be edit
    list_editable = ['phone']
    # filter to help administration search
    list_filter = ['username']
    # Search field when the administrator try to search
    search_fields = ['username', 'description']
    # Help to display or no the field that can be display


admin.site.register(Address)
admin.site.register(UserProfile)
