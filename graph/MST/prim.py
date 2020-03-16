numOfVertex, numOfEdge = map(int, input().split(" "))
graph = [[] for _ in range(0, numOfVertex+1)]
vertex = [[i, float("inf"), i] for i in range(0, numOfVertex+1)]
inQueue = [True for _ in range(0, numOfVertex+1)]
sum = 0

def prim(r):
    vertex[r][1] = 0
    queue = vertex[1:]
    while len(queue) > 0:
        queue.sort(key=lambda x : x[1])
        u = queue.pop(0)
        inQueue[u[0]] = False
        for i in graph[u[0]]:
            if inQueue[i[0]] and vertex[i[0]][1] > i[1]:
                vertex[i[0]][1] = i[1]
                vertex[i[0]][2] = u[0]

for i in range(0, numOfEdge):
    u, v, w = map(int, input().split(" "))
    graph[u].append((v, w))
    graph[v].append((u, w))

prim(1)
for i in range(2, numOfVertex+1):
    sum += vertex[i][1]
    print(f"{vertex[i][0]}<->{vertex[i][2]}: {vertex[i][1]}")
print(sum)