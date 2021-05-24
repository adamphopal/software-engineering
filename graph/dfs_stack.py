vertexList = ['0', '1', '2', '3', '4', '5', '6']
edgeList = [(0,1), (0,2), (1,0) , (1,3) , (2,0) , (2,4) , (2,5) , (3,1), (4,2) , (4,6), (5,2), (6,4)]
graphs = (vertexList, edgeList)

def dfs(graph, start):
    vertexList, edgeList = graph
    visitedVertex = []
    stack = [start]
    adjacencyList = [[] for vertex in vertexList]

    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    while stack:
        current = stack.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedVertex:
                stack.append(neighbor)
        visitedVertex.append(current)
    return visitedVertex

print(dfs(graphs, 0))

#Detect Cycle in Undirect Graph (DFS): while DFS traversal, if an already visited node is found, graph this cycle using dfs.
#interview question? Find the cycle in the graph ? the output should look like this: [0, 2, 5, 4, 6, 1, 3]
