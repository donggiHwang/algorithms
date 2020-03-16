numOfVertex, numOfEdge = map(int, input().split(" "))
graph = [[] for _ in range(0, numOfVertex+1)]
graph_r = [[] for _ in range(0, numOfVertex+1)]
visit = [False for _ in range(0, numOfVertex+1)]
result = []

def DFS(g, v, s):
    visit[v] = True
    for i in g[v]:
        if visit[i] == False:
            DFS(g, i, s)
    s.append(v)

def kosaraju():
    global visit
    stack = []
    scc = []

    for i in range(1, numOfVertex+1):
        if visit[i] == False:
            DFS(graph, i, stack)
    visit = [False for _ in range(0, numOfVertex+1)]
    while len(stack) > 0:
        u = stack.pop()
        if visit[u] == False:
            DFS(graph_r, u, scc)
            result.append(scc)
            scc = []

for i in range(0, numOfEdge):
   u, v = map(int, input().split(" "))
   graph[u].append(v)
   graph_r[v].append(u)

kosaraju()
for i in result:
    print(i)