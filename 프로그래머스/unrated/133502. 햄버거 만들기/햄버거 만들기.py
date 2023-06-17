def solution(ingredients):
    answer = 0
    stack = []
    for ingredient in ingredients:
        if len(stack) >= 3 and ingredient == 1 and (stack[-3],stack[-2],stack[-1])==(1,2,3):
            answer += 1
            for _ in range(3):
                stack.pop()
        else:
            stack.append(ingredient)
    return answer