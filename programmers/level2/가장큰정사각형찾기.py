'''
정사각형의 시작점을 찾으려하니 해결법이 완전탐색밖에 떠오르지 않았다..
관점을 바꿔보자.
정사각형의 마지막 점을 찾는건 어떨까
'''

# 완전탐색 .......
def find_square(x, y, board, answer):
    move=0
    row=len(board)
    col=len(board[0])
    max_row=0
    max_col=0

    while 1:
        if x+1+move < row and y+1+move < col and board[x+1+move][y] and board[x][y+1+move]:
            move+=1
            continue
        max_row=x+move
        max_col=y+move
        break

    if move==0:
        return 0

    count=move-1

    n_x=x
    n_y=y
    while n_x != max_row and n_y != max_col: 
        n_x=n_x+1
        n_y=n_y+1

        if not board[n_x][n_y]:
            return n_x-x-1
        for i in range(1,count+1):
            if n_x+i < row and n_y+i < col and board[n_x+i][n_y] and board[n_x][n_y+i]:
                continue
            else:
                #이전단계로 max값 변경
                max_row=n_x+i-1 
                max_col=n_y+i-1
                count=max_row-n_x-1
                break
        else:
            count=count-1
    return max_row-x

def solution(board):
    answer = 0
    col=len(board[0])
    row=len(board)

    dp=[[0 for i in range(col)] for j in range(row)]

    for i in range(row):
        for j in range(col):
            if i == 0 or j == 0 or board[i][j] == 0:
                dp[i][j] = board[i][j]
                answer=max(dp[i][j], answer)
                continue
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
            answer=max(dp[i][j], answer)

    return answer**2

print(solution([[1]]))
# print(solution([[1,1],[1,1]]))
# print(solution([[1,1,1,1],[1,1,0,1],[1,1,1,1]]))
# print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
# print(solution([[0,0,1,1],[1,1,1,1]]))