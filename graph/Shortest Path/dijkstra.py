numOfVertex, numOfEdge = map(int, input().split(" "))
graph = [[] for _ in range(0, numOfVertex+1)]
vertex = [[i, float("inf"), None] for i in range(0, numOfVertex+1)]


def relax(u, v, w):
    if vertex[v][1] > vertex[u][1] + w:
        vertex[v][1] = vertex[u][1] + w
        vertex[v][2] = u


def dijkstra(s):
    vertex[s][1] = 0
    queue = vertex[1:]
    while len(queue) > 0:
        queue.sort(key=lambda x: x[1])
        u = queue.pop(0)
        for i in graph[u[0]]:
            relax(u[0], i[0], i[1])


for _ in range(0, numOfEdge):
    u, v, w = map(int, input().split(" "))
    graph[u].append([v, w])
dijkstra(1)
for i in range(2, numOfVertex+1):
    print(f"1->{i}: {vertex[i][1]}")
