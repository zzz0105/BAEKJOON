n = int(input())
arr = list(map(int,input().split()))

in_len = [arr[0]] + [1] * (n-1)
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            in_len[i] = max(in_len[i], in_len[j]+arr[i])
        else:
            in_len[i] = max(in_len[i], arr[i])

print(max(in_len))