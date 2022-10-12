import sys

n, m = map(int,sys.stdin.readline().rstrip().split())
words = {}
for _ in range(n):
    tmp = sys.stdin.readline().rstrip()
    words[tmp] = words.get(tmp, 0) + 1
words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for word in words:
    if len(word[0]) >= m:
        print(word[0])