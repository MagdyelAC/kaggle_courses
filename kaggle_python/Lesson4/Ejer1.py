def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L)>1:
        return L[1]
    else:
        return None
    
l=[1,5,2,6]
print(select_second(l))
l=[1]
print(select_second(l))