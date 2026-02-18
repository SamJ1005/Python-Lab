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

#     def operate(self, operator, *numbers):
#         if operator == "+":
#             result = 0
#             for i in numbers:
#                 result += i
#             return result
        
#         elif operator == "*":
#             result = 1
#             for i in numbers:
#                 result *= i
#             return result


# obj = MathOperations()

# op = input("Enter operation (+ or *): ")
# n = int(input("How many numbers? "))

# values = []
# for i in range(n):
#     values.append(int(input("Enter number: ")))

# print("Result =", obj.operate(op, *values))
