n = int(input())
post = input()
nums = [int(input()) for _ in range(n)]
ops = ['+','*','-','/']
stack = []
for p in post:
    if p == '+':
        stack.append(stack.pop()+stack.pop())
    elif p == '-':
        stack.append(-(stack.pop()-stack.pop()))
    elif p == '/':
        stack.append(1/(stack.pop()/stack.pop()))
    elif p == '*':
        stack.append(stack.pop()*stack.pop())
    else:
        stack.append(nums[ord(p)-65])
print('%.2f'%(stack[-1]))