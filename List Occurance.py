items = input("Enter elements separated by space: ").split()
x = input("Enter the element to count: ")

count = items.count(x)

print(f"List: {items}")
print(f"Occurrences of '{x}': {count}")
