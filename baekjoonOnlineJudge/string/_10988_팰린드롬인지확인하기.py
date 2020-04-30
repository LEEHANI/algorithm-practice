'''
s[start:end:step]
'''
s = input()

# answer = 1

# for i in range(int(len(s)/2)):
#     if s[i] != s[-i-1]:
#         answer = 0
#         break
# print(answer)
if s == s[::-1]:
    print(1)
else:
    print(0)
