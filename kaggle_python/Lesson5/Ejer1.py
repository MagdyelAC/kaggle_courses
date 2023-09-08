def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    n=0
    for num in nums:
        if num % 7 == 0:
            return True
        
    return False

l=[1,5,3,6,7]
print(has_lucky_number(l))
l=[1,5,3,6]
print(has_lucky_number(l))