class MathOperations:
    def add(self, *numbers):
        total = 0
        for i in numbers:
            total += i
        return total

obj = MathOperations()
n = int(input("How many numbers to add? "))
values = []

for i in range(n):
    num = int(input("Enter number: "))
    values.append(num)

result = obj.add(*values)
print("Sum =", result)
print("Sum of 2 numbers:", obj.add(5, 10))
print("Sum of 3 numbers:", obj.add(8, 6, 4))
print("Sum of 5 numbers:", obj.add(7, 8, 9, 5, 2))

