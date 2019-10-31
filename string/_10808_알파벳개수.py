def solution(s):
    arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    for i in range(len(arr)):
        alp = arr[i]

        if s.count(alp) == 0:
            print("0", end=" ")
        else:
            print(s.count(alp), end=" ")


solution(input())
