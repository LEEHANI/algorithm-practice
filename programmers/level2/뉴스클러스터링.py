def intersection(arr1, arr2):
    its=list(set(arr1).intersection(arr2))
    s=len(its)
    
    for a in its:
        s+=min(arr1.count(a), arr2.count(a))-1
    
    return s
    
def union(arr1, arr2):
    uni=list(set(arr1).union(arr2))
    s=len(uni)
    
    for a in uni:
        s+=max(arr1.count(a), arr2.count(a))-1
    return s
        
def solution(str1, str2):
    a,b=[],[]
    
    for i in range(len(str1)-1):
        s=str1[i:i+2].lower()
        
        if 'a'<= s[0] <='z' and 'a'<= s[1] <='z':
            a.append(s)
            
    for i in range(len(str2)-1):
        s=str2[i:i+2].lower()
        
        if 'a'<= s[0] <='z' and 'a'<= s[1] <='z':
            b.append(s)       
            
    if len(a)==0 and len(b)==0:
        return 65536
    
    return int(intersection(a,b)/union(a,b)*65536)


# print(solution('FRANCE', 'french'))
# print(solution('handshake', 'shake hands'))
# print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))
# print(solution('aaab', 'aaab'))

