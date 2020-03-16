numOfVertex, numOfEdge = map(int, input().split(" "))
graph = [[] for _ in range(0, numOfVertex+1)]
capacity = [[0 for _ in range(0, numOfVertex+1)] for _ in range(0, numOfVertex+1)]
flow = [[0 for _ in range(0, numOfVertex+1)] for _ in range(0, numOfVertex+1)]
parent = []

def BFS(start, end):
    queue = []
    queue.append(start)
    while len(queue) > 0:
        u = queue.pop(0)
        for v in graph[u]:
            if capacity[u][v] - flow[u][v] > 0 and parent[v] == None:
                queue.append(v)
                parent[v] = u
                if v == end:
                    return

def edmondsKarp(start, end):
    result = 0
    while True:
        global parent
        parent = [None for _ in range(0, numOfVertex+1)] 
        BFS(start, end)
        if parent[end] == None:
            break
        f = float("inf")
        v = end
        while v != start:
            f = min(f, capacity[parent[v]][v] - flow[parent[v]][v])
            v = parent[v]
        v = end
        while v != start:
            if v in graph[parent[v]]:
                flow[parent[v]][v] += f
            else:
                flow[v][parent[v]] -= f
            v = parent[v]
        result += f
    return result

for _ in range(0, numOfEdge):
    u, v, c = map(int, input().split(" "))
    graph[u].append(v)
    capacity[u][v] = c

print(edmondsKarp(1, 6))