import numpy as np

A=np.array([[1,2,3],[4,5,6],[7,8,10]])
B=np.array([[7,8,10],[4,5,6],[1,2,3]])

C=A+B 
E=A-B 

print(C)
print('\n')
print(E)
print('\n')

sum_A=np.sum(A)
sum_B=np.sum(B, axis=0)
sum_C=np.sum(C, axis=1)
print(sum_A)
print(sum_B)
print(sum_C)
print('\n')

D = np.dot(A, B)
print(D)
print('\n')

E=np.sort(C,axis=None).reshape(C.shape)
print(E)
print('\n')

E_transpose = E.T
print(E_transpose)