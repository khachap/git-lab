name = str(input("Enter name: "))
for c in name:
    print(chr(ord(c)+1), end="")
print()