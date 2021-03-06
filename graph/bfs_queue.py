vertexList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edgeList = [(0,1), (1,2), (1,3), (3,4), (4,5), (1,6)]
graphs = (vertexList, edgeList)

def bfs(graph, start):
    vertexList, edgeList = graph
    visitedList = []
    queue = [start]
    adjacencyList = [[] for vertex in vertexList]

    # fill adjacencyList from graph
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    # bfs
    while queue:
        current = queue.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedList:
                queue.insert(0,neighbor)
        visitedList.append(current)
    return visitedList

print(bfs(graphs, 0))


#Detect Cycle in Undirect Graph (BFS): while Breadth First Search (BFS) traveral, if an already visited node is found, graph this cycle using bfs.
#interview question? Find the cycle in the graph using Breadth First Search (BFS)? the output should be: [0, 1, 2, 3, 6, 4, 5]
#interview question:find the shortest path? you can use bfs to find the shortest path using the dykstra algo
