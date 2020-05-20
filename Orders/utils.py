import random
import string

from Orders.models import Order


def id_generator(size=9, chars=string.ascii_letters + string.digits):
    the_id = "".join(random.choice(chars) for x in range(size))
    try:
        order = Order.objects.get(oder_id=the_id)
        id_generator()
    except Order.DoesNotExist:
        return the_id
