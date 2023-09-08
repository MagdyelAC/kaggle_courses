def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
        
    return zip_code.isdigit() and len(zip_code)==5

print(is_valid_zip("12436"))
print(is_valid_zip("1243a"))