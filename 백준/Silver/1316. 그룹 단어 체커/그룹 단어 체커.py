def check():
    word = input()
    last = ''
    check = set()
    for w in word:
        if last != w:
            last = w
            if w in check:
                return False
            check.add(w)
    return True

n = int(input())
cnt = 0
for _ in range(n):
    cnt += check()
print(cnt)