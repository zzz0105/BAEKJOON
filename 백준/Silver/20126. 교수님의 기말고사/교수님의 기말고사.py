import sys

N, M, S = map(int,sys.stdin.readline().rstrip().split())
times = []
test_start = 0
for _ in range(N):
    times.append(tuple(map(int,sys.stdin.readline().rstrip().split())))
times.sort()
for start, time in times:
    if test_start+M <= start:
        break
    test_start = start+time
print(-1 if test_start+M > S else test_start)