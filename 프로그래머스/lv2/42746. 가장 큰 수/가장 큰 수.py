def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x:x*3, reverse=True)
    #num의 인수 값을 3자리수로 맞춘 후 비교하기 위해
    return str(int(''.join(numbers)))
    