import numpy as np
array = np.array([[5, 6, 6, 8],[1, 9, 6, 7], [3, 4, 5, 0], [2, 3, 4, 9]])
print("\n The array given: ")
print(array)

print("Dispaly all the elements excluding first row: ")
print(array[1:])

print("Display all the elements excluding alste column: ")
print(array[ : ,  : -1])

print("Display elements of 1st and 2nd column in 2nd and 3rd row: ")
print(array[ 1 : 3, : 2])

print("Display the elements of 2nd and 3rd column: ")
print(array[ : , 1 : 3])

print("Display elements of 2nd the 3rd elements of 1st row: ")
print(array[ : 1 , 1 : 3 ])