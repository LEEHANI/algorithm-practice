import sys
input = sys.stdin.readline

t=int(input())

for T in range(t):
    h,w,n=map(int,input().split())

    # y 층, x 호수
    x=n//h+1
    y=n%h

    if y==0:
        y=h
        x-=1
    w=str(w)
    x,y=str(x),str(y)

    # 방 번호는 YXX나 YYXX 형태
    if len(x)==1:
        x='0'+x
    print(y+x)


