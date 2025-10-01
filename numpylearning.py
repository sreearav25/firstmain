import numpy as np
import sys

a=np.array([1, 2, 3])
b=np.array([4, 5, 6])   

print("Numpy version:", np.__version__)
print("Python version:", sys.version)   

print("Array a:", a)
print("Array b:", b)    
print("Shape of a:", a.shape)
print("Shape of b:", b.shape)
print("Data type of a:", a.dtype)
print("Data type of b:", b.dtype)
print("Size of a:", a.size)
print("Size of b:", b.size)
print("Number of dimensions of a:", a.ndim)
print("Number of dimensions of b:", b.ndim)
print("Item size of a (in bytes):", a.itemsize)
print("Item size of b (in bytes):", b.itemsize)
print("Total bytes consumed by a:", a.nbytes)
print("Total bytes consumed by b:", b.nbytes)
print("First element of a:", a[0])

c=np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array c:\n", c)
print("Shape of c:", c.shape)
print("Number of dimensions of c:", c.ndim)
print("First row of c:", c[0])
print("First element of the first row of c:", c[0, 0])

print ("Array a + b:", a + b)
print("Array a - b:", a - b)    
print("Array a * b:", a * b)
print("Array a / b:", a / b)
print("Array a ** 2:", a ** 2)
print("Square root of a:", np.sqrt(a))  

d=np.array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])

print (d)
print("Shape of d:", d.shape)   
print("Number of dimensions of d:", d.ndim)
print("First row of d:", d[0])
print("First element of the first row of d:", d[0, 0])
print("Element at row 2, column 3 of d:", d[1, 2])
print("Last element of d:", d[-1, -1])
print("Subarray of d (rows 1-2, columns 1-2):\n", d[0:2, 0:2])
print("All rows, column 2 of d:", d[:, 1])
print("All rows, columns 1-2 of d:\n", d[:, 0:2])

e=np.zeros((3,3))
print("Array of zeros:\n", e )


e=np.ones((3,3),dtype='int8')

print("Array of ones:\n", e)
print("Data type of e:", e.dtype)
print("Shape of e:", e.shape)

f=np.full_like(e, 7)
print("Array full of 7s like e:\n", f)      

g=np.random.random((3,3))
print("Random array g:\n", g)
print("Shape of g:", g.shape)
print("Data type of g:", g.dtype)   


##identitiy matrix
h=np.eye(3)
print("Identity matrix h:\n", h)
print("Shape of h:", h.shape)   
print("Data type of h:", h.dtype)
print("Number of dimensions of h:", h.ndim)
print("Size of h:", h.size)
print("Item size of h (in bytes):", h.itemsize)
print("Total bytes consumed by h:", h.nbytes)

output=np.ones((5,5))
print (output )

z=np.zeros((3,3))
print (z)
z[1,1]=9
print (z)

output[1:-1,1:-1]=z
print (output)

