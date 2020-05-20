from Products.models import ProductCategory
from MarketPlus import settings


# Create your views here.

def market_plus(request):
    return {
        'active_categories': ProductCategory.objects.filter(active=True),
        'site_name': settings.SITE_NAME,
        'meta_keywords': settings.META_KEYWORDS,
        'meta_description': settings.META_DESCRIPTION,
        'request': request
    }
