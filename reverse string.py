text = "hello"
rev = text[::-1]   # slicing to reverse the string
print(rev)

text = "Python"
rev = ""           # empty string to build the reverse

for ch in text:    # take each character
    rev = ch + rev # add each character to the front

print(rev)
