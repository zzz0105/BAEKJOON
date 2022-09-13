n = int(input())
arr = list(map(int,input().split()))
de_len = [1] * n
for i in range(n):
    for j in range(i):
        if arr[i] < arr[j]:
            de_len[i] = max(de_len[i], de_len[j]+1)
print(max(de_len))