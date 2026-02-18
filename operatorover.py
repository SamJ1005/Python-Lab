# class Complex:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def __add__(self, other):
#         return Complex(self.a + other.a, self.b + other.b)

#     def __sub__(self, other):
#         return Complex(self.a - other.a, self.b - other.b)

#     def display(self):
#         print(self.a, "+", self.b, "i")


# print("Enter First Complex Number")
# r1 = int(input("a part: "))
# i1 = int(input("binary part: "))

# print("Enter Second Complex Number")
# r2 = int(input("a part: "))
# i2 = int(input("binary part: "))

# c1 = Complex(r1, i1)
# c2 = Complex(r2, i2)

# add_result = c1 + c2
# sub_result = c1 - c2

# print("\nAddition Result:")
# add_result.display()

# print("Subtraction Result:")
# sub_result.display()

class Complex:

    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __sub__(self, other):
        return Complex(self.r - other.r, self.i - other.i)

    def __str__(self):
        return f"{self.r} + {self.i}i"


r1 = int(input("Enter real part of first number: "))
i1 = int(input("Enter imaginary part of first number: "))

r2 = int(input("Enter real part of second number: "))
i2 = int(input("Enter imaginary part of second number: "))

c1 = Complex(r1, i1)
c2 = Complex(r2, i2)

print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)
