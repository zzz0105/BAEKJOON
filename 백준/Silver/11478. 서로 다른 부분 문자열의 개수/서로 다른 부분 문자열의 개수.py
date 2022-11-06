import sys

s = sys.stdin.readline().rstrip()
result = set()
total =len(s)
for length in range(1,total+1):
    for start in range(total-length+1):
        result.add(s[start:start+length])
print(len(result))