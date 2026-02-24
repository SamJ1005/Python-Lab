filename = input("Enter file name: ")

try:
    file = open(filename, "r")
    content = file.read()
    print("File Content:")
    print(content)
    file.close()

except FileNotFoundError:
    print("File not found")