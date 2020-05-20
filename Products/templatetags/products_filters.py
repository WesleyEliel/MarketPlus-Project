from django import template
import locale

register = template.Library()


@register.filter(name='currency')
def currency(value):
    try:
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    except:
        locale.setlocale(locale.LC_ALL, '')
    loc = locale.localeconv()
    return locale.currency(value, loc['currency_symbol'], grouping=True)


@register.filter(name='addcss')
def addcss(value, arg):
    print(value)
    css_classes = value.field.widget.attrs.get('class', '').split(' ')

    if css_classes and arg not in css_classes:
        css_classes = "%s %s" % (css_classes, arg)
    return value.as_widget(attrs={'class': css_classes})


@register.filter(name='add_aria_describedby')
def add_aria_describedby(value, arg):
    aria_describedby = value.field.widget.attrs.get('aria-describedby', '').split(' ')
    if aria_describedby and arg not in aria_describedby:
        aria_describedby = "%s %s" % (aria_describedby, arg)
    return value.as_widget(attrs={'aria-describedby': aria_describedby})


@register.filter(name='add_placeholder')
def add_placeholder(value, arg):
    print(value)
    placeholder = value.field.widget.attrs.get('placeholder', '').split(' ')
    print(placeholder)
    if placeholder and arg not in placeholder:
        placeholder = "%s %s" % (placeholder, arg)
    return value.as_widget(attrs={'aria-describedby': placeholder})

@register.filter(name='list_range')
def list_range(value, arg):
    return range(value)
