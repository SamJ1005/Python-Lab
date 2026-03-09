import numpy as np

# User input
n = int(input("Enter number of elements: "))

print("Enter elements of first array:")
a = []
for i in range(n):
    a.append(int(input()))

print("Enter elements of second array:")
b = []
for i in range(n):
    b.append(int(input()))

# Convert to NumPy arrays
arr1 = np.array(a)
arr2 = np.array(b)

# Arithmetic operations
print("\nAddition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)

# Universal functions
print("\nSquare root of first array:", np.sqrt(arr1))
print("Exponential of first array:", np.exp(arr1))