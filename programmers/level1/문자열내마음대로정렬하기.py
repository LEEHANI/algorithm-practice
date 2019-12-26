'''
https://stackoverflow.com/questions/13669252/what-is-key-lambda
'''
def solution(strings, n):
    # for i,string in enumerate(strings):
    #     strings[i] = string[n] + strings[i]
    # strings.sort()    
    # return [string[1:] for string in strings]
    return sorted(strings, key=lambda x: x[n])

print(solution(['sun','bed','car'],1))