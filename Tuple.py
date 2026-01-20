n = int(input("Enter atleast 5 elements in the tuple: "))
tup = ()
for i in range(n):
    value = input("Enter a value: ")
    tup += (value,)
    
print("Elements in tuple:")
for item in tup:
    print(item)

value = input("Enter a value to search: ")
found = False
for i in range(len(tup)):
    if tup[i] == value:
        print(f"Value '{value}' found at index {i}")
        found = True
        break
if not found:
    print("Value not found in tuple.")

print("Total elements in tuple:", len(tup))