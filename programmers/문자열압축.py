def try_answer(arr):
    answer = ''
    target = arr.pop(0)
    cnt_same_s = 1

    while len(arr):
        compare = arr.pop(0)

        if target == compare:
            cnt_same_s += 1
            continue

        if cnt_same_s > 1:
            answer.append(str(cnt_same_s))

        answer.append(target)
        target = compare
        cnt_same_s = 1

    if cnt_same_s > 1:
        answer.append(str(cnt_same_s))
    answer.append(compare)

    # print('try_answer ', ''.join(answer), len(''.join(answer)))

    return len(answer)


def solution(s):
    answer = 1000
    split_len = len(s)//2

    if not split_len:
        return 1

    while split_len >= 1:
        arr = []

        for i in range(0, len(s), split_len):
            arr.append(s[i:i+split_len])

        result = try_answer(arr)
        answer = result if answer > result else answer
        split_len -= 1

    return answer


# print(solution('aabbaccc'))
# print(solution('ababcdcdababcdcd'))
# print(solution('abcabcdede'))
# print(solution('abcabcabcabcdededededede'))
# print(solution('xababcdcdababcdcd'))
# print(solution('aaaaaaaaaaaa'))
# print(solution('abcabc'))
# print(solution('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
# print(solution('a'*10))
# print(solution('abbbbbbbbc'))
print(solution('a'))
