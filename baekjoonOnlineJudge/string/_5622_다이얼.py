s = input()

answer = 0
for _s in s:
    if _s in ["A", "B", "C"]:
        answer += 3
    elif _s in ["D", "E", "F"]:
        answer += 4
    elif _s in ["G", "H", "I"]:
        answer += 5
    elif _s in ["J", "K", "L"]:
        answer += 6
    elif _s in ["M", "N", "O"]:
        answer += 7
    elif _s in ["P", "Q", "R", "S"]:
        answer += 8
    elif _s in ["T", "U", "V"]:
        answer += 9
    elif _s in ["W", "X", "Y", "Z"]:
        answer += 10
print(answer)
