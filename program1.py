import numpy as np

#--------------------->  Array creation <--------------------------------------------

arr=np.array([1,2,3,4,5,6])
print(arr)

arr1=np.zeros((2,2))
print(arr1)  

arr2=np.ones((3,3))
print(arr2)

arr3=np.arange(0,10,1)
print(arr3)

#---------------------->  Mathematical operations <-----------------------------------

arr4=np.sum(arr)
print(arr4)

arr5=np.mean(arr)
print(arr5)

arr6=np.square(arr)
print(arr6)

arr7=np.sin(arr)
print(arr7)

#----------------------> Reshaping and Transposing <-----------------------------------

arr8=np.arange(1,21).reshape(2,10)
print(arr8)


print(arr8.T)


#-----------------------> Accessing and slicing  <--------------------------------------

arr = np.array([10, 20, 30, 40, 50])
print("Element at index 2:", arr[2])
print("Slice from index 1 to 3:", arr[1:4])

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Element at [1, 2]:", matrix[1, 2])
print("First row:", matrix[0])
print("Second column:", matrix[:, 1])



#-------------------------> Concatenation snd stacking <---------------------------------

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Concatenation
concat = np.concatenate((arr1, arr2))
print("Concatenated Array:", concat)

# Stacking
stacked = np.vstack((arr1, arr2))
print("Stacked Vertically:\n", stacked)


#---------------------------> Conditional selection <-------------------------------------

arr=np.array([1,2,3,4,5,6,7,8,9])

print(arr[arr%2==0])


#---------------------------> Random number generation <-----------------------------------

random_array=np.random.rand(2,2)

print(random_array)