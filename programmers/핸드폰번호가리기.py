def solution(phone_number):
    answer = ''
    # 리팩토링 전
    # for i in range(0, (len(phone_number)-4), 1):
    # answer += '*'
    # answer += phone_number[-4:]
    answer += '*'*(len(phone_number)-4)+phone_number[-4:]
    return answer


print(solution("027778888"))
