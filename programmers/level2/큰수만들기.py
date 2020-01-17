def find_max(number):
    idx,max=0,0
    for i,n in enumerate(map(int,number)):
        if n==9:
            return i,9
        if n > max:
            idx,max=i,n
    return idx,max

def solution(number, k):
    answer = ''
    answer_len = len(number) - k
    while len(answer) < answer_len:
        idx,m=find_max(number[:k+1])
        k=k-idx
        answer+=str(m)
        number=number[idx+1:]
        
        if k==0:
            answer += number
    return answer

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("999999", 1))