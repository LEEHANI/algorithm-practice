'''
prime number = 1과 자기 자신을 약수로 갖는 수 
'''

# 1 무난한 알고리즘 이지만 오래걸림 
def solution(n):
    answer = []
    for i in range(2,n+1,1):
        prime=i
        for j in range(2, i//2+1, 1):  
            if i%j==0:
                prime=0
                break
        if prime != 0:        
            answer.append(prime)
    return len(answer)

# 2 아리토스테네스의 체 
def solution2(n):
    answer = []
    
    eratosthenes=list(range(0,n+1))
    
    for i in range(2, n+1):
        if eratosthenes[i]==0:
            continue
        else:
            answer.append(eratosthenes[i])
            
            for j in range(eratosthenes[i], n+1, eratosthenes[i]):
                eratosthenes[j]=0
    return len(answer)

print(solution2(10))