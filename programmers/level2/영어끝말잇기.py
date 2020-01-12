def solution(n, words):
    for i in range(len(words)-1):
        k=i+2
        if words[i][-1] == words[i+1][0]:
            for j in range(i):
                if words[j] == words[i+1]:
                    return [n if k%n == 0 else k%n, k//n+1 if k%n != 0 else k//n]  
        else:
            return [n if k%n == 0 else k%n, k//n+1 if k%n != 0 else k//n]
    return [0, 0]

print(solution(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))
print(solution(5, ['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive']))
print(solution(2, ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']))
