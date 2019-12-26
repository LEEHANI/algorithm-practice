def solution(a, b):
    month=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day=['MON','TUE','WED','THU','FRI','SAT','SUN']
    return day[(sum(month[:a-1])+b)%7]
print(solution(1,1))
print(solution(5,24))
