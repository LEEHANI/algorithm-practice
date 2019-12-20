def solution(drum):

    answer = 0

    size = len(drum[0])
    # print(drum)
    # arr = []

    # for d in drum:
    #     arr.append(list(d))
    for i in range(size):
        x, y = 0, i
        starFlag = 0

        while x < size:  # x가 6이면 while문에서 빠져나가야함.
            ring = drum[x][y]
            # print(ring, x, y)

            if ring == "#":
                x += 1
            elif ring == ">":
                y += 1
            elif ring == "<":
                y -= 1
            elif ring == "*" and starFlag == 1:
                break
            elif ring == "*" and starFlag == 0:
                x += 1
                starFlag += 1

        if x == size:
            answer += 1

    return answer


drum = ["######", ">#*###", "####*#", "#<#>>#", ">#*#*<", "######"]

print(solution(drum))
