
import math
import numpy as np
def cxnt(n):
    return [ x**2 for x in range(1,n**2) if (x**2<n**2) ] 


def decompose(n):
    k=0
    
    L1=cxnt(n)
    Q=[1,L1[-1]]
    X1=n**2
    if n %2==0:

        xb=(n+1)**2-L1[-1]-1
    else:
        xb=xb=n**2-L1[-1]

    
    for h in range(5):
        
        print(L1)
        L=[x for x in L1 if ( x<=(xb))]
        
        if (L!=[] and (L[-1] not in Q) ):
            Q.append(L[-1])
            k+=L[-1]
        
            L1=L
            if n%2==0:

                xb-=L1[-1]-1
            else:
                sb-=L1[-1]

        Q.sort()
        
    return Q
        


print(np.sqrt(decompose(50)))
