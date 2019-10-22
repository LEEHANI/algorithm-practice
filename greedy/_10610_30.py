'''
[기본적으로 알고있어야 할 사항]
3의 배수 판별법: 모든 수를 더해서 3의 배수이면 된다. ex) 숫자가 123일때 1+2+3 = 6 이므로 3의 배수이다.

[알고리즘]
30의 배수가 되려면 
1. 숫자 0이 있어야한다. 
2. 3의 배수여야 한다.
3. 큰 수를 만들기 위해 내림차순 정렬
'''


N = input()
arr = list(map(int, list(N)))


def func():
    if sum(arr) % 3 != 0 or arr.count(0) == 0:
        return -1

    arr.sort(reverse=True)

    temp = ""

    for i in arr:
        temp += str(i)

    return int(temp)


print(func())
