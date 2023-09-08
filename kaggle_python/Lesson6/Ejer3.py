from e2 import *
def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    mult={}
    for key in keywords:
        lst=word_search(doc_list,key)
        mult[key]=lst
    return mult

print(multi_word_search(["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"],['casino', 'they']))