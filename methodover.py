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

# class MathOperations:
#     def add(self, *numbers):
#         total = 0
#         for num in numbers:
#             total += num
#         return total

# obj = MathOperations()

# print("Sum of 2 numbers:", obj.add(5, 10))
# print("Sum of 3 numbers:", obj.add(1, 2, 3))
# print("Sum of 5 numbers:", obj.add(4, 5, 6, 7, 8))

