"""
나누기3, 나누기2, 뺴기1 모두 가능한 숫자가 입력될 경우,
각 연산들 사이에 우선 순위가 없음을 고려해야한다.
그러므로, 각 연산마다 수행 횟 수를 구하고, 그들 사이의
최솟값을 구해야 하는 것이 중요하다
"""
n = int(input())


def makeOne(n):
    x = [0, 0]
    for i in range(2, n+1):
        minimum = x[i-1]+1
        if i % 3 == 0:
            minimum = min(x[int(i/3)]+1, minimum)
        if i % 2 == 0:
            minimum = min(x[int(i/2)]+1, minimum)
        x.append(minimum)
    return x[n]


print(makeOne(n))
