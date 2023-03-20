from itertools import combinations

word = input()
combis = combinations(range(len(word)-1),2)
answer = '|'
for l, r in combis:    # ex) abcdefg (1,3) -> ab cd efg
    answer = min(word[l::-1] + word[r:l:-1] + word[-1:r:-1], answer)
print(answer)