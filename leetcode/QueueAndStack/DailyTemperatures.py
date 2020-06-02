T = [47,47,47,47]

# 시간 초과 
def brute_force(T):
    answer=[]

    for i in range(len(T)):
        target=T[i]
        cnt=0
        for j in range(i+1, len(T)):
            cnt+=1
            if target<T[j]:
                answer.append(cnt)
                break
        else:
            answer.append(0)
    return answer

# stack 내부를 증가하는 수열로 만들자
# 넣으려는 값이 내부 값보다 크다면 갖고있을 이유가 없다. 
# 값이 클수록 커버할 수 있는 따뜻함이 많아지기 때문이다. 
#
# T=[2,7,5,9] t=2, stack = [7,5,9] 라면 5는 필요 없다. 
# t가 2일 때 확인해야 할 건 7이기 때문이다. 
#
# 배열 맨 마지막부터 시작
# target = 73, stack = [(7,73)]
# target = 76, stack = [(6,76)], target > stack[0...size] stack.pop()  
# ex) ㅁ
def increaseStack(T):
    size=len(T)-1
    stack=[[size,T.pop()]]
    answer=[0]

    while T:
        target = T.pop()
        size-=1

        while stack and stack[-1][1]<=target:
            stack.pop()
        if stack:
            answer.append(stack[-1][0]-size)
        else:
            answer.append(0)
        stack.append([size,target])

    answer.reverse()

    return answer

# print(brute_force(T))
print(increaseStack(T))