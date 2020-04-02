'''
대각선이 지날 때 w의 개수와 h의 개수만큼 사용해서 지나간다. 

참고하면 좋은 블로그
https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%A9%80%EC%A9%A1%ED%95%9C-%EC%82%AC%EA%B0%81%ED%98%95-in-python

'''
def solution(w,h):
    
    total=int(w*h)
    remove=0

    g=gcd(w,h)

    w=w//g
    h=h//g
    remove=(w+h-1)*g
      
    return int(total-remove)

def gcd(a, b):

    temp = a 

    while b!=0:
        temp=a 
        a=b
        b=temp%b
    return a
    

print(solution(8,12))