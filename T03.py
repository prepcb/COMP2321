import numpy as np

A = np.array([[1,1,1,1],[0,1,-2,0],[-3,1,0,0]])


def VsV(a,b,n):
    return(b - a*(b[n]/a[n]))


print(VsV(A[0,:],A[2,:],0))

#for i in range(2):#
   # for j in range(i+1,3):
       # A[j,:] = VsV(A[i,:],A[i+j,:],i)

print(A)

print(np.matmul(np.array([1,2,3]),np.array([[2,3],[3,4],[3,5]])))
