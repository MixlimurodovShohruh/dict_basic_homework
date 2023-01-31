def cities_dict(cities:list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
    """ 
    d={}
    f=0
    while f<len(cities): 
        for i in cities:
            d.setdefault(f,i)
            f+=1
    return d
print(cities_dict(["Bukhara", "Khiva", "Namangan", "Samarkand", "Tashkent"]))