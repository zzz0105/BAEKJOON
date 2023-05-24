from collections import deque, defaultdict

def compare(word_a, word_b):
    if len(word_a)!=len(word_b):
        return False
    cnt = 0
    for i in range(len(word_a)):
        if word_a[i]!=word_b[i]:
            cnt += 1
    return True if cnt==1 else False

def solution(begin, target, words):
    dic = defaultdict(list)

    for word in words:
        if compare(begin, word):
            dic[begin].append(word)
        
    for i in range(len(words)):
        for j in range(i, len(words)):
            if compare(words[i], words[j]):
                dic[words[i]].append(words[j])
                dic[words[j]].append(words[i])

    q = deque([(begin, 0)])
    visited = {begin}
    while q:
        now, step = q.popleft()
        if now == target:
            return step
        for next_word in dic[now]:
            if next_word not in visited:
                q.append((next_word, step+1))
                visited.add(next_word)
    return 0