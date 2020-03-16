numOfTestcase = int(input())
for i in range(0, numOfTestcase):
    n = int(input())
    def plus123(n):

        r = [0, 1, 2, 4]
        for i in range(4, n+1):
            r.append(r[i-1]+r[i-2]+r[i-3])
        return r[n]
    print(plus123(n))
