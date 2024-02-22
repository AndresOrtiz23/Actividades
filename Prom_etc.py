import math
def dist_l1(u : list,v: list) -> float:
    '''
    Retorna la distancia del taxista
    
    Argumentos:
    u=lista
    V=lista
    Retorna
    float
    >>> dist_l1([5,6,9],[8,9,2])
    39
    >>> dist_l1([3, 5, 7], [2, 4, 6])
    27
    >>> dist_l1([0, 0, 0], [0, 0, 0])
    0
    '''
    if len(u)==len(v):
        a=0
        for i in range (len(v)):
            a=a+abs(u[i]+v[i])
        return a


def dist_l2(u,v):
    '''
    Retorna la distancia euclidiana
    
    Argumentos:
    u=lista
    V=lista
    Retorna
    float
    >>> dist_l2([5,6,9],[8,9,2])
    8.18535277187245
    >>> dist_l2([1, 2, 3], [4, 5, 6])
    5.196152422706632
    >>> dist_l2([0, 0, 0], [0, 0, 0])
    0.0
    >>> dist_l2([-1, -1, -1], [1, 1, 1])
    3.4641016151377544
    '''
    if len(u)==len(v):
        a=0
        for i in range (len(v)):
            a=a+((u[i]-v[i])**2)
        a=math.sqrt(a)
        return a

def dist_l3(u,v):
    """
    Calcula la distancia Chebyshev
    
    Argumentos:
    u=lista
    V=lista
    
    Retorna
    float

    >>> dist_l3([1, 2, 3], [4, 5, 6])
    3
    >>> dist_l3([0, 0, 0], [0, 0, 0])
    0
    >>> dist_l3([-1, -1, -1], [1, 1, 1])
    2
    >>> dist_l3([3, 5, 7], [2, 4, 6])
    1
    """
    if len(u)==len(v):
        a=[None]*len(v)
        for i in range (len(v)):
            a[i]=abs(u[i]-v[i])
        return max(a)
def promedio(u):
    """
    Calcula el promedio de los elementos en una lista.

    Args:
    u (list): La lista de elementos.

    Returns:
    float: El promedio de los elementos en la lista u.

    >>> promedio([1, 2, 3, 4, 5])
    3.0
    >>> promedio([10, 20, 30, 40, 50])
    30.0
    >>> promedio([2, 4, 6, 8, 10])
    6.0
    >>> promedio([0, 0, 0, 0, 0])
    0.0
    """
    k=len(u)
    a=0
    for i in range (k):
        a=a+u[i]
    a=a/k
    return a
def desv_est(u):
    """
    Calcula la desviación estándar de una lista de elementos.

    Args:
    u (list): La lista de elementos.

    Returns:
    float: La desviación estándar de los elementos en la lista u.

    >>> desv_est([1, 2, 3, 4, 5])
    1.4142135623730951
    >>> desv_est([10, 20, 30, 40, 50])
    14.142135623730951
    >>> desv_est([2, 4, 6, 8, 10])
    2.8284271247461903
    >>> desv_est([0, 0, 0, 0, 0])
    0.0
    """
    f=promedio(u)
    k=len(u)
    a=0
    for i in range (k):
        a=a+((u[i]-f)**2)
    a=math.sqrt(a/k)
    return a
def varianza(u):
    """
    Calcula la varianza de una lista de elementos.

    Args:
    u (list): La lista de elementos.

    Returns:
    float: La varianza de los elementos en la lista u.

    >>> varianza([1, 2, 3, 4, 5])
    2.0000000000000004
    >>> varianza([10, 20, 30, 40, 50])
    200.00000000000003
    >>> varianza([2, 4, 6, 8, 10])
    8.000000000000002
    >>> varianza([0, 0, 0, 0, 0])
    0.0
    """
    a=(desv_est(u)**2)
    return a

import doctest
doctest.testmod(verbose=True)

