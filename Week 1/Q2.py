import numpy as np

def replaceOdd(a):
    for i in range(a.size):
        if a[i]%2==1:
            a[i]=-1
    return a 

a=np.arange(10)
print(replaceOdd(a))