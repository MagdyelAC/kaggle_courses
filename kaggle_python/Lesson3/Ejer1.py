def sign (n):
    if n<0:
        return -1
    elif n>0:
        return 1
    else :
        return 0
    
print(sign(4))
print(sign(-1))
print(sign(0))