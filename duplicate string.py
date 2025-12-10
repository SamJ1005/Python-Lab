items = []
size = int(input("Enter number of items: "))

for i in range(size):
    item = input("Enter item: ")
    items = items + [item]  

unique_items = []
for item in items:
    found = False
    for u in unique_items:
        if item == u:
            found = True
            break

    if not found:
        unique_items = unique_items + [item] 

print("List after removing duplicates:")
print(unique_items)