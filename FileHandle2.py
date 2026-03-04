n = int(input("How many items to be in the list? "))

items = []

for i in range(n):
    value = input("Enter item: ")
    items.append(value + "\n")

# Write list to file
f = open("list.txt", "w")
f.writelines(items)
f.close()

# Read file
f = open("list.txt", "r")
print("\nItems in file:")
print(f.read())
f.close()
