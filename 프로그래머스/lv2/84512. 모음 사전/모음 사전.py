def solution(word):
    answer = 0
    alpha_dic = {'A':1, 'E':2, 'I':3, 'O':4, 'U':5}
    n = [781, 156, 31, 6, 1] #i번째 자릿수가 바뀌기 위해 움직여야 하는 횟수
    for i in range(len(word)):
        answer += n[i] * (alpha_dic[word[i]]-1) + 1
    return answer