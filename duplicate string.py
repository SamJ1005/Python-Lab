items = ["apple", "banana", "apple", "orange", "banana"]
unique = []   

for item in items:       # look at each item
    if item not in unique:   # only add if not already in unique
        unique.append(item)

print(unique)
