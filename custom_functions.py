def flatten_list(*args):
    """
    It take one or more variables any type or list with variables or
    list items inside and return a one dimension list (or a flatten array).

    :param args: one or more variables any type

    :return: list
    """
    flatten = []
    for _ in args:
        for i in _:
            if type(i) == list:
                flatten.extend(flatten_list(i))
            else:
                flatten.append(i)
    return flatten

