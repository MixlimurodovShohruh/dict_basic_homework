def first_item():
    """
    Given a dictionary, Return first item value.
    """
    data = {'a': 1, 'b': 2}
    for i in data:
        return data[i]
        
print(first_item())