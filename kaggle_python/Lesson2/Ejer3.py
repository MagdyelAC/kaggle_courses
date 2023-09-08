def to_smash(total_candies,n=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91,3)
    1
    """
    return total_candies % n

print(to_smash(91,2))
print(to_smash(90))