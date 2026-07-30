import numpy as np

def first4col(a):
    result=[]
    for i in range(a.shape[0]):
        row=[]
        for j in range(4):
            row.append(a[i][j])
        result.append(row)
    
    return np.array(result)

print(first4col(np.arange(100).reshape(5,-1)))