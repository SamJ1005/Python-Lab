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
