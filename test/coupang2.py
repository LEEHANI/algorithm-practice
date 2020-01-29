import itertools

def solution(N,M,T,K):
    
    answer=0
    arr=list(range(0,M+1,1))
    
    for i in itertools.product(arr, repeat=N):
        info = list(i)
        if sum(info)==M:            
            for j in range(len(info)):
                if sum(info[j:j+T]) > K:
                    break
            else:
                print("all pass", info, T, K)
                answer+=1
    return answer
            
# print(solution(2,4,1,3)) #3
print(solution(4,7,2,4)) # 28
# print(solution(4,7,2,3)) # 0
