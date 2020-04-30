s = input()

for i in s:
    temp = ord(i)-3

    if temp < ord('A'):
        temp += 26
    print(chr(temp), end="")
