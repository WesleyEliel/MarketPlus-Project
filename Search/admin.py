from django.contrib import admin

# Register your models here.
from Search.models import SearchTerm


class SearchTermAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'ip_address', 'search_date')
    list_filter = ('ip_address', 'user', 'q')
    exclude = ('user',)


admin.site.register(SearchTerm, SearchTermAdmin)
