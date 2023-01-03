from collections import Counter

name = sorted(Counter(input()).items(), key=lambda x:x[0])
answer = ''
center = ''
flag = False
for c, t in name:
    answer += c*(t//2)
    if t%2:
        if center:
            flag = True
            break
        else:
            center = c

print('I\'m Sorry Hansoo' if flag else answer+center+answer[::-1])