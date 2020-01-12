'''
solution([40, 40, 40],100) 케이스에 런타임 에러 발생
이유: front가 가리키는 인덱스와 people[-1]의 인덱스가 일치할 때 문제 발생
해결 if (len(people)-1) == front:

'''
def solution(people, limit):
    answer = 0
    
    people.sort()
    front=0
    while front!=len(people):
        
        if (len(people)-1) == front:
            return answer+1
        
        if len(people) >= 2 and people[front]+people[-1] <= limit:
            front+=1
        people.pop()
        answer+=1   
             
    return answer
# print(solution([70,50,80,50],100))
# print(solution([70,80,50],100))
# print(solution([70],100))
print(solution([40, 40, 40],100))