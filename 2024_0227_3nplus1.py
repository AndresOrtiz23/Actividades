def three_n_plus1(n):
    """
    #correccion, faltaba agregar un ">"
    >>> three_n_plus1(5)
    5
    
    """
    i=0
    while(n!=1):
        if(n%2==0): #correcion, faltaban ":" despues del if
            n=n/2
            i+=1
        else:
            n=3*n+1
            i+=1
    return print(i) #Se agrego un print para que se muestre el numero
    
import doctest
doctest.testmod(verbose=True)
