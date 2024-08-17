'''
O código abaixo não é usual, implementei apenas para critério de estudo.
'''

def soma(a, b):
    """Soma a e b

    >>> soma(10, 20)
    30

    >>> soma(-10, 20)
    10

    >>> soma('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: 'a' precisa ser int ou float
    """
    assert isinstance(a,(int,float)), "'a' precisa ser int ou float"
    assert isinstance(b,(int,float)), "'b' precisa ser int ou float"
    return a + b

def subtrai(x, y):
    """Soma x e y

    >>> subtrai(10, 20)
    -10

    >>> subtrai(-10, 20)
    -30

    >>> subtrai('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: 'x' precisa ser int ou float
    """
    assert isinstance(x,(int,float)), "'x' precisa ser int ou float"
    assert isinstance(y,(int,float)), "'y' precisa ser int ou float"
    return x - y    



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)