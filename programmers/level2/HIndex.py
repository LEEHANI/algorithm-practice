def solution(citations):
    point=len(citations)//2
    citations=sorted(citations, reverse=True)
    
    while 1:
        try:
            if citations[point-1] >= point and citations[point] <= point:
                return point
            elif citations[point-1] > point and citations[point] > point:
                point+=1
            else:
                point-=1
        except IndexError as identifier:
            return point

# print(solution([3,0,6,1,5]))
# print(solution([1, 0]))
# print(solution([22, 42]))
print(solution([1]))