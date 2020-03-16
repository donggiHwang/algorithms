numOfTest = int(input())
for i in range(0, numOfTest):
    n = int(input())

    def fibonacci(n):
        c = [(1, 0), (0, 1)]
        for i in range(2, n+1):
            numOfZero = c[i-1][0] + c[i-2][0]
            numOfOne = c[i-1][1] + c[i-2][1]
            c.append((numOfZero, numOfOne))
        return c[n]
    result = fibonacci(n)

    print(f'{result[0]} {result[1]}')
