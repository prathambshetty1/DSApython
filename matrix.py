import numpy as np

A= np.array([[2,1,3],
            [1,0,2],
            [4,1,8]])
B= np.array([[1,2,1],
             [0,1,0],
             [3,1,2]])
dot_result=np.dot(A,B)

Inverse_A=np.linalg.inv(A)
print("Dot Product:\n",dot_result)
print("Inverse of A:\n",Inverse_A)