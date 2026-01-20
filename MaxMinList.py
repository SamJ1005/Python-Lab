n = int(input("Enter how many numbers: "))

numbers = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

largest = max(numbers)
smallest = min(numbers)

print("List:", numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)
