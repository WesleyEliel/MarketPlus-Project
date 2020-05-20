from django import template
from Blog.forms import SearchForm
import urllib

register = template.Library()


@register.inclusion_tag("tags/blog_search.html")
def blog_search(request):
    query = request.GET.get('query', '')
    form = SearchForm({'query': query})
    return {'form': form}

