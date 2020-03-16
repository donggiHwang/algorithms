numOfVertex, numOfEdge = map(int, input().split(" "))
edge = []
distance = [float("inf") for _ in range(0, numOfVertex+1)]
parent = [None for _ in range(0, numOfVertex+1)]

def relax(u, v, w):
    if distance[v] > distance[u] + w:
        distance[v] = distance[u] + w
        parent[v] = u

def bellmanFord(s):
    distance[s] = 0
    for i in range(0, numOfVertex):
        for i in edge:
            ((u, v), w) = i
            relax(u, v, w)
    for i in edge:
        ((u, v), w) = i
        if distance[v] > distance[u] + w:
            return False
    return True

for _ in range(0, numOfEdge):
    u, v, w = map(int, input().split(" "))
    edge.append(((u, v), w))

if bellmanFord(1):
    for i in range(2, numOfVertex+1):
        print(f"1->{i}: {distance[i]}")
else:
    print("negative cycle exist")