def solution(s):
    answer = []
    tp=s[2:-2].split("},{")
    tp=sorted(tp, key=len)
    answer.append(tp[0])
    for num_list in tp[1:]:
        for num in num_list.split(','):
            if num not in answer:
                answer.append(num)
                break

    return list(map(int,answer))

# print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
# print(solution("{{123}}"))
# print(solution("{{20,111},{111}}"))
print(solution(	"{{2},{2,1},{2,1,3},{2,1,3,4}}"))