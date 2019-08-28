# Numpy Arrays
import numpy as np

# list = [1,2,3,4,5]
# print(list)

# arr = np.array(list)
# print(arr)

# # 2 dimensional array
# list = [[1,2,3],[1,2,3],[1,2,3]]
# arr = np.array(list)
# print(arr)

# # Array generator
# print(np.arange(0,10))
# print(np.arange(0,10,2))

# # Array of 0's
# print( np.zeros(5) )
# print( np.zeros((5,5)) )

# # Array of 1's
# print( np.ones(5) )
# print( np.ones((5,5)) )

# # linspace -> equally spaced points (start , end , no. of points)
# print( np.linspace(0,5,10) )

# # Creating an identity matrix
# print( np.eye(4) )

# # Array of random numbers 0-1
# print( np.random.rand(5))
# print( np.random.rand(5,5))
# # From -1 - 1
# print( np.random.randn(5))
# print( np.random.randn(5,5))

# # Random Integer
# print( np.random.randint(0,100)) #Returns a single integer
# print( np.random.randint(0,100,10)) #Returns an array of integers

# # Changing the dimensions of an array
# arr = np.random.randint(0,50,25)
# print(arr)
# print(arr.reshape(5,5))
# #  ***The no of elements in the matrix should be equal to the size of the linear array

# # Max Min in an array
# arr = np.random.randint(0,100,50)
# print(arr)
# print(arr.max())
# print(arr.min())
# # Index of Max and Min
# print(arr.argmax())
# print(arr.argmin())

# # Find the size of the array
# arr= np.arange(0,52)
# print(arr.shape)

# # Data type of the array
# arr = np.arange(0,52)
# print(arr.dtype)


# ******************************************************************************************

# # Numpy Array Indexing & Slicing
# * 1D Array
# arr = np.arange(0,11)
# print(arr)
# print(arr[5])
# print(arr[0:4])
# print(arr[:5])
# print(arr[5:])

# # Broadcasting -> Altering values
# arr = np.arange(0, 11)
# print(arr)
# sliced = arr[:5]
# print(sliced)
# sliced[:]  = 100
# print(sliced)
# print(arr) # <- *** the values also gets changed here
# # Instead use the copy method
# sliced = arr.copy()
# sliced[:]=100
# print(sliced)
# print(arr)

# # 2D array
# # arr = np.arange(0,9)
# # arr = arr.reshape(3,3)

# # INSTEAD
# arr = np.arange(0,9).reshape(3,3)
# print(arr)
# # Indexing
# print(arr[2][2])
# # OR
# print(arr[2,2])

# # 2D Array slicing
# arr = np.arange(0,9)
# arr = arr.reshape(3,3)
# print(arr , end="\n*****\n")
# print(arr[:2]  ,end="\n*****\n")
# print(arr[:2 , :2] )

# # Comparision Operators
# arr = np.arange(1,11)
# print(arr)
#
# bool_arr = arr > 5
# print(bool_arr)
# # *Now to get the true values from arr
# print( arr[bool_arr] )

# COMPACTED
# print( arr[arr < 7] )




# ******************************************************************************************


# # OPERATIONS
# arr = np.arange(0,11)
# print(arr)

# print(arr+arr)
# print(arr-arr)
# print(arr*arr)
# print(arr ** 2)

# # SCALAR OPERATIONS
# print(arr+100)
# print(arr-100)
# print(arr*100)

# # FUNCTIONS
# print(np.sqrt(arr))
# print(np.exp(arr))
# print(np.max(arr))
# print(np.sin(arr))
# print(np.log(arr))










