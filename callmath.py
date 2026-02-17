import createmath

print("Mathematical Operations Module")
a = float(input("\nEnter first number: "))
b = float(input("Enter second number: "))

print("\nAddition:", createmath.add(a, b))
print("Subtraction:", createmath.subtract(a, b))
print("Multiplication:", createmath.multiply(a, b))
print("Division:", createmath.divide(a, b))
print("Power:", createmath.power(a, b))
print("Modulus:", createmath.modulus(a, b))
