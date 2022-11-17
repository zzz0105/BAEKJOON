chars = input()
bomb = input()
n = len(bomb)
stack = []
for c in chars:
    stack.append(c)
    if len(stack)>=n and stack[-1]==bomb[-1]:
        if ''.join(stack[-n:]) == bomb:
            del stack[-n:]
print(''.join(stack) if stack else 'FRULA')