from numpy import random


# array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# array2 = np.array([[1, 2, 3, 4], [6, 7, 8, 9]])

# print(array[1:8])
# print(array2[1,0])

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)