def repeatedString(s, n):
    size=len(s)
    c=s.count('a')
    count=c*(n//size)+s[0:n%size].count('a')
    
    return count 

print(repeatedString('aba',10))