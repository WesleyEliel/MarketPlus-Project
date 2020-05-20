from django import template

register = template.Library()

@register.inclusion_tag("tags/review_form_tag.html")
def review_form_tag(form_field):
    return {'form_field': form_field}
