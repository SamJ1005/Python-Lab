tup = (10, 35, 271, 7, 50,)

print("Tuple:", tup)

print("Elements in tuple:")
for item in tup:
    print(item)

value = int(input("Enter a value to search: "))
if value in tup:
    index = tup.index(value)
    print(f"Value {value} found at index {index}")
else:
    print("Value not found in tuple.")

print("Total elements in tuple:", len(tup))
