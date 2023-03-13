def choose(ans):
    global min_ans, max_ans
    if len(ans)==k+1:
        now = ''.join(map(str,ans))
        min_ans = min(min_ans, now)
        max_ans = max(max_ans, now)
        return
    for n in range(0,10):
        if len(ans)==0 or (inequality[len(ans)-1]=='<' and ans[-1]<n) or (inequality[len(ans)-1]=='>' and ans[-1]>n):
            if n not in ans:
                ans.append(n)
                choose(ans)
                ans.pop()

k = int(input())
inequality = input().split()
min_ans, max_ans = '999', '000'
choose([])
print(max_ans, min_ans, sep='\n')