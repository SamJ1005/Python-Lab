text = input("Enter text to write into file: ")

f = open("sample.txt", "w")
f.write(text)
f.close()

# Read using seek()
f = open("sample.txt", "r")
f.seek(0)
print("\nContent after writing:")
print(f.read())
f.close()

# Append new data
more_text = input("\nEnter text to append: ")
f = open("sample.txt", "a")
f.write("\n" + more_text)
f.close()
f = open("sample.txt", "r")
print("\nFinal file content:")
print(f.read())
f.close()
