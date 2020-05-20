from Search.models import SearchTerm
from Products.models import Product
from django.db.models import Q

from Stats import stats

STRIP_WORDS = ['a', 'an', 'and', 'by', 'for', 'from', 'in', 'no', 'not', 'of', 'on', 'or', 'that', 'the', 'to', 'with']


# store the search text in the database

def store(request, q):
    term = None
    # if search term is at least three chars long, store in db
    if len(q) > 2:
        term = SearchTerm()
        term.q = q
        term.ip_address = request.META.get('REMOTE_ADDR')
        term.tracking_id = stats.tracking_id(request)
        term.user = None
        print(request.user)
        try:
            term.user = request.user
        except:
            pass
        term.save()


# get products matching the search text
def products(search_text):
    words = _prepare_words(search_text)
    product = Product.objects.filter(active=True)
    results = {'products': []}
    # iterate through keywords
    for word in words:
        products = product.filter(Q(title__icontains=word) | Q(description__icontains=word) |
                                  Q(other_notes__icontains=word) | Q(category__name=word) |
                                  Q(category__product_title__icontains=word) |
                                  Q(category__product_theme_writing__icontains=word))
        results['products'] = products
    return results


# strip out common words, limit to 5 words
def _prepare_words(search_text):
    words = search_text.split()
    for common in STRIP_WORDS:
        if common in words:
            words.remove(common)
        return words[0:5]
