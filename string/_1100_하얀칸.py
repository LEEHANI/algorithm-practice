answer = 0

for i in range(8):
    temp = input()

    for j in range(8):
        if ((i+j) % 2 == 0) and temp[j] == "F":
            answer += 1
print(answer)
