def countingValleys(n, s):
    current=1
    count=0
    for i in s:
        if i == 'U':
            current +=1
            if current == 1:
                count+=1
        else:
            current -=1
        # print(current)
    return count

print(countingValleys(8, 'UDDDUDUU'))
# print(countingValleys(12, 'DDUUDDUDUUUD'))