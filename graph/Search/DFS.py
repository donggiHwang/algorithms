numOfVertex, numOfEdge = map(int, input().split(" "))
graph = [[] for i in range(0, numOfVertex+1)]
visit = [False for i in range(0, numOfVertex+1)]

def DFS(v):
    visit[v] = True
    for u in graph[v]:
        if visit[u] == False:
            print(f"{v}->{u}")
            DFS(u)

for i in range(0, numOfEdge):
   u, v = map(int, input().split(" "))
   graph[u].append(v)

for i in range(1, numOfVertex+1):
    if visit[i] == False:
        DFS(i)