print("\nUser Built-in Class Operator Overloading")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Using built-in add class:", int.__add__(x, y))
print("Using built-in mul class:", int.__mul__(x, y))
s = input("Enter a string: ")
n = int(input("Enter number of times to repeat string: "))
print("Using built-in mul class for string:", str.__mul__(s, n))

class A:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __mul__(self, other):
        return self.value * other.value

print("\nUser Defined Class Operator Overloading")
r1 = int(input("Enter first value: "))
r2 = int(input("Enter second value: "))
ob1 = A(r1)
ob2 = A(r2)

print("Using + operator:", ob1 + ob2)
print("Using * operator:", ob1 * ob2)
