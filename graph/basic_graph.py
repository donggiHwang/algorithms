numOfVertex, numOfEdge = map(int, input().split(" "))
graph = [[] for i in range(0, numOfVertex+1)]

for i in range(0, numOfEdge):
    u, v = map(int, input().split(" "))
    graph[u].append(v)

for i in range(0, numOfVertex):
    for j in graph[i]:
        print(f"{i}->{j}")