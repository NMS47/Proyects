def max_of_three(n1: int, n2: int, n3: int):
    """
    Return the max value of the three.

    :param n1: first num.
    :param n2: second num.
    :param n3: third num.
    :return: the higher number.
    """
    if n1 > n2:
        if n1 > n3:
            return n1
        else:
            return n3
    else:
        if n2 > n3:
            return n2
        else:
            return n3


print(max_of_three(4, 11, 10))
