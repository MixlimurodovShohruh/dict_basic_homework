def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    dict={}
    number=0
    alpha=0
    for i in txt:
        if i.isalpha():
            alpha+=1
        elif i.isdigit():
            number+=1
    dict.setdefault("LETTERS",alpha)
    dict.setdefault("DIGITS",number)
    return dict
print(count_all("Hello World"))