n = int(input())
s = []
s.append([input() for _ in range(n)])

for i in range(n):
    target = s[0][i]
    for j in range(i, n, 1):
        compare = s[0][j]
        if(target == compare[::-1]):
            print(len(target), target[int(len(target)/2)])
            break
