import sys

n = int(sys.stdin.readline().rstrip())

scores_max = [[0]*3 for _ in range(2)]
scores_min = [[0]*3 for _ in range(2)]

for i in range(n):
    tmp = tuple(map(int,sys.stdin.readline().rstrip().split()))

    scores_max[1][0] = max(scores_max[0][0],scores_max[0][1]) + tmp[0]
    scores_min[1][0] = min(scores_min[0][0],scores_min[0][1]) + tmp[0]

    scores_max[1][1] = max(scores_max[0][0],scores_max[0][1],scores_max[0][2]) + tmp[1]
    scores_min[1][1] = min(scores_min[0][0],scores_min[0][1],scores_min[0][2]) + tmp[1]

    scores_max[1][2] = max(scores_max[0][1],scores_max[0][2]) + tmp[2]
    scores_min[1][2] = min(scores_min[0][1],scores_min[0][2]) + tmp[2]

    scores_max[0] = scores_max[1][:]
    scores_min[0] = scores_min[1][:]

print(max(scores_max[-1]), min(scores_min[-1]))