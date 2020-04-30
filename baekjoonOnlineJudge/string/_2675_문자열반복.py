# https://www.acmicpc.net/problem/2675

T = int(input())

for i in range(T):
    r, s = input().split()

    for c in s:
        print(c * int(r), end="")
    print()
