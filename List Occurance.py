items = []
n = int(input("Enter the range: "))

for i in range(n):
    item = input("Enter an element: ")
    items.append(item)

x = input("Enter the element to count: ")
count = items.count(x)

print(f"List: {items}")
print(f"Occurrences of '{x}': {count}")