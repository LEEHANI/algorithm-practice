import sys
input=sys.stdin.readline
n=int(input())
# n=5
arr=[]
answer=0
for i in range(n):
    arr.append(list(input()))

# arr=[['1','1','1','0','0'],
#     ['2','#','#','#','1'],
#     ['3','#','#','#','1'],
#     ['2','#','#','#','1'],
#     ['1','2','2','1','0']]

# 모서리
# if arr[0][0]=='1':
    # arr[1][1]='*'
# if arr[0][n-1]=='1':
    # arr[1][n-2]='*'

# if arr[n-1][0]=='1':
    # arr[n-2][1]='*'
# if arr[n-1][n-1]=='1':
    # arr[n-2][n-2]='*'

top_x=[1,1,1]
top_y=[-1,0,1]
left_x=[-1,0,1]
left_y=[1,1,1]
right_x=[-1,0,1]
right_y=[-1,-1,-1]
bottom_x=[-1,-1,-1]
bottom_y=[-1,0,1]

# for a in arr:
#     print(a)
# print()

def top(i,j,target):
    global answer
    count=0
    for k in range(3):
        nx=top_x[k]+i
        ny=top_y[k]+j
        if 0<=nx<n and 0<=ny<n and ny != n-1 and j != n-1:
            if count==target and arr[nx][ny]!='*':
                arr[nx][ny]='!' #다른데서 못바꾸게 하기
            if arr[nx][ny] == '*':
                count+=1
            elif count!=target and arr[nx][ny] == '#':
                arr[nx][ny]='*'
                answer+=1
                count+=1
def left(i,j,target):
    global answer
    count=0
    for k in range(3):
        nx=left_x[k]+i
        ny=left_y[k]+j
        if 0<=nx<n-1 and 0<=ny<n-1 and ny != n-1:
            if count==target:
                arr[nx][ny]='!' #다른데서 못바꾸게 하기
            if arr[nx][ny] == '*':
                count+=1
            elif count!=target and arr[nx][ny] == '#':
                arr[nx][ny]='*'
                answer+=1
                count+=1

def right(i,j,target):
    global answer
    count=0
    for k in range(3):
        nx=right_x[k]+i
        ny=right_y[k]+j
        if 0<=nx<n and 0<=ny<n and ny != 0:
            if count==target and arr[nx][ny]=='#':
                arr[nx][ny]='!' #다른데서 못바꾸게 하기
            if arr[nx][ny] == '*':
                count+=1
            elif count!=target and arr[nx][ny] == '#':
                arr[nx][ny]='*'
                answer+=1
                count+=1

def bottom(i,j,target):
    global answer
    count=0
    for k in range(3):
        nx=bottom_x[k]+i
        ny=bottom_y[k]+j
        if 0<=nx<n and 0<=ny<n and nx != n-1:
            if count==target and arr[nx][ny]=='#':
                arr[nx][ny]='!' #다른데서 못바꾸게 하기
            if arr[nx][ny] == '*':
                count+=1
            elif count!=target and arr[nx][ny] == '#':
                arr[nx][ny]='*'
                answer+=1
                count+=1

for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            target=int(arr[i][j])

        if i==0: # 위쪽
            top(i,j,target)
            # print('top',remain_close)
        elif j==0: #왼쪽
            left(i,j,target)
            # print('l',remain_close)
        elif j==n-1: #오른쪽 
            right(i,j,target)
            # print('r',remain_close)
        elif i==n-1: #밑쪽
            bottom(i,j,target)
            # print('b',remain_close)
        
        if 2<=i<n-2 and 2<=j<n-2:
            answer+=1
# for i in arr:
#     print(i)
print(answer)

