from collections import deque

t = int(input())
for _ in range(t):
    p = input()
    n = int(input())
    flag = 1
    cnt = 0
    nums = deque(input()[1:-1].split(','))
    if n == 0:
        nums = deque()
    for i in range(len(p)):
        if p[i] == 'R':
            cnt+=1
        elif p[i]=='D':
            if nums:
                if cnt%2:
                    nums.pop()
                else:
                    nums.popleft()
            else:
                flag = 0
                print('error')
                break

    if flag == 0:
        continue
    else:
        if cnt%2:
            nums.reverse()
            print('['+ ','.join(nums)+']')
        else:
            print('['+ ','.join(nums)+']')
