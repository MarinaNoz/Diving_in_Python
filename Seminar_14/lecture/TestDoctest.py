def is_prime(p: int) -> bool:
    '''
    Проверим является ли число Р простым, найдя остаток от деления в диапазоне [2, P)
    >>> is_prime(42)
    False
    >>> is_prime(73)
    True
    '''

    for i in range(2, p):
        if p % 2 == 0:
            return False
    return True


if __name__ == '__main__':
    import doctest
    # doctest.testmod()
    doctest.testmod(verbose=True)
