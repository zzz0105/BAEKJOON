def bt(d, answer):
    if d == N+1:
        if eval(answer.replace(' ','')) == 0:
            print(answer)
        return
    for op in ' +-':
        answer += op+str(d)
        bt(d+1,answer)
        answer = answer[:-2]

tc = int(input())
for _ in range(tc):
    N = int(input())
    bt(2,'1')
    print()