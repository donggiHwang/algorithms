numOfVertex, numOfEdge = map(int, input().split(" "))
graph = [[] for i in range(0, numOfVertex+1)]
indegree = [0 for i in range(0, numOfVertex+1)]
result = []

def topologicalSort():
    queue = []
    c = 0
    for i in range(1, numOfVertex+1):
        if indegree[i] == 0:
            queue.append(i)
            result.append(i)
    while len(queue) > 0:
        u = queue.pop(0)
        c += 1
        for i in graph[u]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
                result.append(i)
    if c < numOfVertex:
        print("cycle")

for i in range(0, numOfEdge):
    u, v = map(int, input().split(" "))
    graph[u].append(v)
    indegree[v] += 1
topologicalSort()

for i in result:
    print(i)