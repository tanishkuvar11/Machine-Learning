import numpy as np

def compare(x, y):
    greater=[]
    equal=[]
    for i in range(x.size):
        if x[i]>y[i]:
            greater.append(i)
        elif x[i]==y[i]:
            equal.append(i)

    return np.array(greater), np.array(equal)

a=np.array([21, 64, 86, 22, 74, 55, 81, 79, 90, 89])
b=np.array([21, 7, 3, 45, 10, 29, 55, 4, 37, 18])
print(compare(a,b))