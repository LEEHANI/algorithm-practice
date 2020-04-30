n = int(input())
answer = 0

for i in range(n):
    stack = []
    for char in input():
        stack.append(char)
        try:
            if stack[-1] == stack[-2]:
                stack.pop(-1)
                stack.pop(-1)
        except IndexError as identifier:
            pass
    if len(stack) == 0:
        answer += 1
print(answer)
