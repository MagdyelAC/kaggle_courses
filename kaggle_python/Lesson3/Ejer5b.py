def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not(ketchup or mustard or onion)

print(wants_plain_hotdog(True,True,False))
print(wants_plain_hotdog(False,False,False))