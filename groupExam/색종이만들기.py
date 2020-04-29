'''
인덱스 실수하지 말자.. 
end_x//2를 하면 중간값을 한번만 얻을 수 있다
'''
import sys
sys.setrecursionlimit(2**20)
input=sys.stdin.readline

n=int(input())
arr=[]
blue=0
white=0

for i in range(n):
    arr.append(list(map(int,input().split())))


def make_color(start_x, start_y, end_x, end_y):

    if start_x > end_x or start_y > end_y:
        return
    
    result = color_check(start_x, start_y, end_x, end_y)
    
    if (start_x+1, start_y+1) == (end_x, end_y):
        return

    if not result:
        middle_x = (start_x + end_x)//2
        middle_y = (start_y + end_y)//2 

        make_color(start_x, start_y, middle_x, middle_y)
        make_color(start_x, middle_y, middle_x, end_y)
        make_color(middle_x, start_y, end_x, middle_y)
        make_color(middle_x, middle_y, end_x, end_y)
    else:
        return

def color_check(start_x, start_y, end_x, end_y):
    global white
    global blue 

    check = arr[start_x][start_y]

    for i in range(start_x,end_x):
        for j in range(start_y, end_y):
            if arr[i][j] == check:
                continue
            else:
                return False

    if check == 0:
        white+=1
    else:
        blue+=1

    return True


make_color(0,0,n,n)
print(white)
print(blue)