import copy
numOfVertex = int(input())
graph = []
distance = []


def floydWarshall():
    distance = copy.deepcopy(graph)
    for k in range(0, numOfVertex):
        for i in range(0, numOfVertex):
            for j in range(0, numOfVertex):
                distance[i][j] = min(
                    distance[i][j], distance[i][k] + distance[k][j])
    return distance


def iToD(c):
    if c == "inf" or c == "INF":
        return float("inf")
    else:
        return int(c)


for i in range(0, numOfVertex):
    graph.append(list(map(iToD, input().split(" "))))

distance = floydWarshall()
for i in distance:
    print(i)
