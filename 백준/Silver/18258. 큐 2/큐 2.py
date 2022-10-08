from collections import deque
import sys
n = int(sys.stdin.readline().rstrip())
que = deque()
for _ in range(n):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == 'push':
        que.append(command[1])
    elif command[0] == 'pop':
        print(que.popleft() if que else -1)
    elif command[0] == 'size':
        print(len(que))
    elif command[0] == 'empty':
        print(0 if que else 1)
    elif command[0] == 'front':
        print(que[0] if que else -1)
    elif command[0] == 'back':
        print(que[-1] if que else -1)