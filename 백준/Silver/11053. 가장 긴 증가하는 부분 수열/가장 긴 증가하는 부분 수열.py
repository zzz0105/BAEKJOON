n = int(input())
arr = list(map(int,input().split()))
in_len = [1] * n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            in_len[i] = max(in_len[i], in_len[j]+1)
print(max(in_len))