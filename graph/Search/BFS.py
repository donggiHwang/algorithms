numOfVertex, numOfEdge, start = map(int, input().split(" "))
graph = [[] for i in range(0, numOfVertex+1)]
visit = [False for i in range(0, numOfVertex+1)]

def BFS(s):
    queue = []
    visit[s] = True
    queue.append(s)
    while len(queue) > 0:
        u = queue.pop(0)
        for i in graph[u]:
            if visit[i] == False: 
                visit[i] = True
                queue.append(i)
                print(f"{u}->{i}")

for i in range(0, numOfEdge):
    u, v = map(int, input().split(" "))
    graph[u].append(v)

BFS(start)