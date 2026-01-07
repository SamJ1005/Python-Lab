text = input("Enter a string: ")
count = {}             # empty dictionary to store counts

for ch in text:        # go through each character
    if ch in count:    # if character already counted
        count[ch] = count[ch] + 1
    else:              # if character appears for the first time
        count[ch] = 1

print("Character frequency:")
for key in count:
    print(key, ":", count[key])