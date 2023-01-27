def oldest(people:dict):
    """
    Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    """
    d=0
    f=0
    for i in people:
        x = people[i]
        if x>d:
            d= x
            f = i

    return f
people={"Javohir": 22, "Sharof": 23, "Tolib": 34, "Rustam": 16}
print(oldest(people))