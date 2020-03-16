numOfVertex, numOfEdge = map(int, input().split(" "))
parent = [0 for _ in range(0, numOfVertex+1)]
edge = []
MST = []
sum = 0

def makeSet(x):
    parent[x] = x

def findSet(x):
    if parent[x] != x:
        parent[x] = findSet(parent[x])
    return parent[x]

def unionSet(x, y):
    px = findSet(x)
    py = findSet(y)

    if px < py:
        parent[py] = px
    else:
        parent[px] = py

def kruskal():
    for i in range(1, numOfVertex+1):
        makeSet(i)
    edge.sort(key=lambda x : x[1])
    for i in edge:
        if findSet(i[0][0]) != findSet(i[0][1]):
            MST.append(i)
            unionSet(i[0][0], i[0][1])
    
for i in range(0, numOfEdge):
    u, v, w = map(int, input().split(" "))
    edge.append(((u, v), w))

kruskal()
for i in MST:
    sum += i[1]
    print(f"{i[0][0]}<->{i[0][1]}: {i[1]}")
print(sum)