numOfVertex, numOfEdge = map(int, input().split(" "))
graph = [[] for _ in range(0, numOfVertex+1)]
discover = [float("inf") for _ in range(0, numOfVertex+1)]
finished = [False for _ in range(0, numOfVertex+1)]
stack = []
result = []
dCnt = 1

def DFS(v):
    global dCnt
    discover[v] = dCnt
    dCnt += 1
    sccRoot = discover[v]
    stack.append(v)
    for i in graph[v]:
        if discover[i] == float("inf"):
            sccRoot = min(sccRoot, DFS(i))
        elif finished[i] == False:
            sccRoot = min(sccRoot, discover[i])
    if discover[v] == sccRoot:
        scc = []
        while True:
            u = stack.pop()
            scc.append(u)
            finished[u] = True
            if u == v:
                break
        result.append(scc)
    return sccRoot

def tarjan():
    for i in range(1, numOfVertex+1):
        if discover[i] == float("inf"):
            DFS(i)

for i in range(0, numOfEdge):
    u, v = map(int, input().split(" "))
    graph[u].append(v)

tarjan()
for i in result:
    print(i)