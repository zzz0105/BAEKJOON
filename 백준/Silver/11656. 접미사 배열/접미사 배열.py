word = input()
suffix = []
for i in range(len(word)):
    suffix.append(word[i:])
print(*sorted(suffix), sep='\n')