'''
좌, 우로 움직일 때 A가 아닌 알파벳을 먼저 찾아, 그 방향으로 움직이도록 짜는 게 핵심
'''
def solution(name):
    answer = 0
    name=list(name)
    cursor=0

    while name.count('A') != len(name):
        if name[cursor] != 'A':
            answer+=min(ord(name[cursor])-ord('A'), 26-ord(name[cursor])+ord('A')) 
            name[cursor] = 'A'

        if name.count('A') == len(name):
            return answer

        front_move=1
        end_move=1

        for i in range(1,len(name)):
            if name[cursor+i] == 'A':
                front_move+=1
            else:
                break
            if name[cursor-i] == 'A':
                end_move+=1
            else:
                break

        print(cursor, front_move, end_move)
        if front_move <= end_move:
            answer+=front_move
            cursor+=front_move
        else:
            answer+=end_move
            cursor-=end_move

    return answer

# print(solution("JEROEN")) #56
print(solution("JAN")) #23
# print(solution("AZA"))
# print(solution("AZAA"))
# print(solution("A"))
# print(solution("AAAAAAA"))
# print(solution("JAABAN"))
# print(solution("AAAB"))
# print(solution("AZAAAZ"))
# print(solution("AAAZAAZA"))