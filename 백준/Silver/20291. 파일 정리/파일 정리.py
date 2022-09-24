n = int(input())
cnt = {}
for _ in range(n):
    a, b = input().split('.')
    cnt[b] = cnt.get(b, 0) + 1
for c in sorted(cnt):
    print(c, cnt[c])