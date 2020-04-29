'''
+-*/
operator [2,1,2,1]라 가정할때 그냥 백트래킹을 진행해본다고 생각해보자. 
그렇게 되면 연산자가 이렇게 선택될 것이다.

첫번째 recursion
+, +, -, *, *, /
+, +, -, *, /, * ....

두번째 recursion
+, +, -, *, *, /
+, +, -, *, /, * ....

세번째 recursion
-, +, +, -, / ...

즉, 연산자가 중복으로 되어있으니 그만큼 똑같은 일을 한다.

'''

n=int(input())

arr=list(map(int,input().split()))
operator=[]
operators=list(map(int,input().split()))
for i in range(operators[0]):
    operator.append('+')
for i in range(operators[1]):
    operator.append('-')
for i in range(operators[2]):
    operator.append('*')
for i in range(operators[3]):
    operator.append('//')
visited=[0]*(n)
min_num=1000000001
max_num=-1000000001

def improved_def(depth, val, add, minus, multiple, divide):
    global min_num
    global max_num

    if depth == len(operator):
        min_num=min(min_num,val)
        max_num=max(max_num,val)
        return

    if add:
        improved_def(depth+1, val+arr[depth+1], add-1, minus, multiple, divide)
    if minus:
        improved_def(depth+1, val-arr[depth+1], add, minus-1, multiple, divide)
    if multiple:
        improved_def(depth+1, val*arr[depth+1], add, minus, multiple-1, divide)
    if divide:
        improved_def(depth+1, int(val/arr[depth+1]), add, minus, multiple, divide-1)

improved_def(0,arr[0], operators[0], operators[1], operators[2], operators[3])
    

def dfs(depth, val):
    global min_num
    global max_num

    if depth == len(operator):
        min_num=min(min_num,val)
        max_num=max(max_num,val)
        return
    else:
        for i in range(len(operator)):
            if not visited[i]:
                visited[i] = 1

                if operator[i] == '+':
                    dfs(depth+1, val+arr[depth+1])
                elif operator[i] == '-':
                    dfs(depth+1, val-arr[depth+1])
                elif operator[i] == '*':
                    dfs(depth+1, val*arr[depth+1])
                elif operator[i] == '//':
                    if val<0 and arr[depth+1] > 0:
                        dfs(depth+1, -(abs(val)//arr[depth+1]))
                    else:
                        dfs(depth+1, val//arr[depth+1])

                visited[i] = 0

# dic={0:'+', 1:'-', 2:'*', 3:'//'}
# # + - * /
# for i in range(4):
#     if operators[i] > 0:
#         visited[operator.index(dic[i])]=1
#         if dic[i] == '//' and arr[0]<0 and arr[1] > 0:
#             dfs(1, -eval(str(abs(arr[0])) + dic[i] + str(arr[1])))
#         else:
#             dfs(1, eval(str(arr[0]) + dic[i] + str(arr[1])))
#         visited[operator.index(dic[i])]=0

print(max_num)
print(min_num)