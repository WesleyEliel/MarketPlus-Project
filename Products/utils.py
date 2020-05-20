from Carts.models import *



# Define utils functions


def price_filter(query_set, min, max):
    pass
def rating_filter(query_set):
    pass
def color_filter(query_set, color):
    pass
def popularity_filter(query_set):
    pass
def newness_filter(query_set):
    pass
def price_increase_gradient_filter(query_set):
    pass
def price_decrease_gradient_filter(query_set):
    pass

"""def price_filter():
def price_filter():
def price_filter():
def price_filter():
    """

def list_to_queryset(model, data):
    from django.db.models.base import ModelBase

    if not isinstance(model, ModelBase):
        raise ValueError(
            "%s must be Model" % model
        )
    if not isinstance(data, list):
        raise ValueError(
            "%s must be List Object" % data
        )

    pk_list = [obj.pk for obj in data]
    return model.objects.filter(pk__in=pk_list)


def show_cart_in_panel(request):
    try:
        the_id = request.session['cart_id']
        print(the_id)
    except KeyError:
        the_id = None
    except:
        the_id = None
    empty = None
    cart = None
    print(the_id)
    if the_id:
        try:
            cart = Carts.objects.get(session_id=the_id)
            try:
                request.session['total_items'] = cart.cartitems_set.count()
            except TypeError:
                pass
            empty = False
        except Carts.DoesNotExist:
            total = None
            try:
                total = request.session['total_items']
            except:
                pass
            if total:
                del request.session['total_items']
            empty = True
    else:
        empty = True
        cart = None
    return empty, cart


def remove_duplicate(entry_list):
    new_list = []
    for items in entry_list:
        if items not in new_list:
            new_list.append(items)
    return new_list