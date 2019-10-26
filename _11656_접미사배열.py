'''
python 문자열 연습 

arr를 초기화 안할 시, append() 함수 사용
'''


def solution(s):
    arr = []
    for i in range(len(s)):
        arr.append(s[i:])

    arr.sort()

    for i in range(len(s)):
        print(arr[i])


S = input()
solution(S)
