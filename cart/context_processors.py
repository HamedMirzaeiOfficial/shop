from .cart import Cart

"""
Add something to all templates. this is just like request, ...
"""


def cart(request):
    return {'cart': Cart(request)}
