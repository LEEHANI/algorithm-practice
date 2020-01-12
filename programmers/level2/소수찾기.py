from itertools import permutations

def solution(numbers):
    answer = 0
    make_numbers=[]
    
    # 조합해서 숫자 만들기
    for i in range(1, len(numbers)+1):
        for num in permutations(numbers, i):
            make_numbers.append(int(''.join(num)))
            
    make_numbers=list(set(make_numbers))
    
    for number in make_numbers:
        if number < 2:
            continue
        
        for i in range(2, number//2+1):
            if number%i==0:
                break
        else:
            print(number)
            answer+=1    
    
    return answer

# print(solution("17"))
# print(solution("011"))
# print(solution("3"))
print(solution("2"))