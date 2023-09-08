def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return (ketchup and not mustard) or (not ketchup and mustard)

print(exactly_one_sauce(True,False,False))
print(exactly_one_sauce(False,False,False))