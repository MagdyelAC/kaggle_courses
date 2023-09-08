def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    return (ketchup and not (mustard or onion))or (mustard and not (ketchup or onion)) or (onion and not (mustard or ketchup))

print(exactly_one_topping(True,False,True))
print(exactly_one_topping(True,False,False))