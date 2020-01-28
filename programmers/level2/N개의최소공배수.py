'''
최소공배수=a*b//최대공약수(a,b)
'''
from math import gcd

def solution(arr):
    
    while len(arr)!=1:
        a=arr.pop()
        b=arr.pop()
        
        arr.append(a*b//gcd(a,b))
    
    return arr[0]

print(solution([2,6,8,14]))