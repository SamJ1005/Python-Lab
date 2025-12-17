def add(num1, num2=22):
    return num1 + num2
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

print("The sum of keyword arguments is:", add(a, b))
print("The sum of default arguments is:", add(a))