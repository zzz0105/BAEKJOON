def solution(s):
    def strange(word):
        ans = ''
        for i in range(len(word)):
            ans += word[i].lower() if i%2 else word[i].upper()
        return ans
    return ' '.join(map(strange, s.split(' ')))