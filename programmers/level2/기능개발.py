def solution(progresses, speeds):
    answer = []
    done=0
    while sum(answer) != len(progresses):
        today=0
        for i in range(len(progresses)):
            if progresses[i] >= 100 and done==i:
                today+=1
                done +=1
                continue
            progresses[i]+=speeds[i]
        if today:
            answer.append(today)    
    return answer

print(solution([93,30,55],[1,30,5]))