import numpy as np 

def conv(a):
    return a.reshape(3, -1)

a=np.arange(12)
print(conv(a))