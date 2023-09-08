def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    return not onion

print(onionless(True,True,False))
print(onionless(True,True,True))

def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup and mustard and onion

print(wants_all_toppings(True,True,True))
print(wants_all_toppings(True,True,False))