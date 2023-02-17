from django import template
'''
register = template.Library()

@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys()
    for item_id in keys:
        if int(item_id) == product.item_id
        return cart.get(item_id)
    return 0
    '''