class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __sub__(self, other):
        return Complex(self.r - other.r, self.i - other.i)

    def __str__(self):
        if self.i >= 0:
            return f"{self.r} + {abs(self.i)}i"
        else:
            return f"{self.r} - {abs(self.i)}i"

r1 = int(input("Enter real part of first number: "))
i1 = int(input("Enter imaginary part of first number: "))

r2 = int(input("Enter real part of second number: "))
i2 = int(input("Enter imaginary part of second number: "))

c1 = Complex(r1, i1)
c2 = Complex(r2, i2)

print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)
