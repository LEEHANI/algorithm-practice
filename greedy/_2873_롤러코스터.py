def func3(r, c):
    x, y = find_min()
    answer = ''
    after_answer = ''
    sx, sy = 0, 0
    ex, ey = r-1, c-1
    # r*c 행렬
    while(sx+2 <= x):
        answer += "R"*(c-1) + "D" + "L"*(c-1)+"D"
        sx += 2
    while (ex-2 >= x):
        after_answer += "D"+"L"*(c-1)+"D"+"R"*(c-1)
        ex -= 2

    # 2*c 행렬 모양
    while sy+2 <= y:
        answer += "DRUR"
        sy += 2
    while ey-2 >= y:
        after_answer = "RURD" + after_answer
        ey -= 2

    # 2*2 행렬모양
    if sx+1 == x:
        answer += "RD"
    else:
        answer += "DR"

    answer += after_answer

    return answer


def func2(r, c):
    answer = ("D"*(r-1) + "R" + "U"*(r-1)+"R")*(c//2)+"D"*(r-1)
    return answer


def func1(r, c):
    answer = ("R"*(c-1) + "D" + "L"*(c-1)+"D")*(r//2)+"R"*(c-1)
    return answer


def find_min():
    min = 1000
    min_r = 0
    min_c = 0
    for i in range(c):
        for j in range(r):
            if (i+j) % 2 == 1:
                if min > arr[i][j]:
                    min = arr[i][j]
                    min_r = i
                    min_c = j

    return min_r, min_c


r, c = map(int, input().split())

arr = []

for i in range(r):
    arr.append(list(map(int, input().split())))

if r % 2 == 1:
    print(func1(r, c))
# col이 홀수일 때,
elif c % 2 == 1:
    print(func2(r, c))
# 둘 다 짝수일 때,
else:
    print(func3(r, c))
