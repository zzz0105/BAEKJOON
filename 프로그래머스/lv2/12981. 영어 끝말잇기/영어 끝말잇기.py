def solution(n, words):
    answer = [0, 0]
    used = set([words[0]])

    for i in range(1, len(words)):
        if words[i-1][-1]==words[i][0] and words[i] not in used:
            used.add(words[i])
        else:
            answer = [i%n+1, i//n+1]
            break

    return answer