import sys 
input = sys.stdin.readline

n,m=map(int,input().split())
pins=[]
# S J I Z 
director=[[0,1],[0,-1],[1,0],[-1,0]]
for i in range(n):
    pins.append(list(map(int,input().split())))
op=input()
x,y=0,0
for i in range(m):
    nx,ny=0,0
    if op[i]=='S':
        nx,ny=director[0]
    elif op[i]=='J':
        nx,ny=director[1]
    elif op[i]=='I':
        nx,ny=director[2]
    elif op[i]=='Z':
        nx,ny=director[3]
    x+=nx
    y+=ny

    # 맨해튼 거리 구하기
    distance=0
    for pin in pins:
        # print(pin, x,y)
        distance+=abs(pin[0]-x)+abs(pin[1]-y)
    print(distance)