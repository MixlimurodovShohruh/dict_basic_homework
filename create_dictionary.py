def create_dictionary(key, value):
    """
    Convert two lists into a dictionary
    Args:
        key(list): list of keys
        value(list): list of values
    Returns:
        dict: dictionary with keys and values
    """
    s={}
    for i in range(len(key)):
        s[key[i]]=value[i]
    return s
print(create_dictionary([1, 2, 3],["one", "two", "three"]))
        