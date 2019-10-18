"""
File: testcourses.py

Sam Bluestone and Zahin Reaz
Builds a graph of the courses in the CS curriculum at W&L
"""

from modules.graph import LinkedDirectedGraph
from modules.linkedStack import LinkedStack
from modules.linkedQueue import LinkedQueue
from modules.grid import Grid
from modules.arrays import Array
from modules.infinity import *
from modules.dijkstraEntry import DijkstraEntry




def makeLabelTable(graph):
    """Returns a table (dictionary) associating vetrex labels with
    index positions."""
    table = {}
    index = 0
    for vertex in graph.vertices():
        table[vertex.getLabel()] = index
        index += 1
    return table

def makeDistanceMatrix(graph, table):
    """Returns a distance matrix for the given graph."""
    matrix = Grid(len(graph), len(graph), INFINITY)
    for vertex in graph.vertices():
        vertexLabel = vertex.getLabel()
        vertexIndex = table[vertexLabel]
        for edge in vertex.incidentEdges():
            neighborLabel = edge.getConnectedTo().getLabel()
            neighborIndex = table[neighborLabel]
            if edge:
               weight = edge.getWeight()
            else:
               weight = INFINITY
            matrix[vertexIndex][neighborIndex] = weight
    return matrix

def printDistanceMatrix(matrix, table):
    labels = Array(len(table))
    position = 0
    for label in table:
        labels[table[label]] = label
        position += 1
    print(" " * 14 + "".join(["{s:^{w}}".format(s=x, w=10)for x in labels]))
    print(" " * 14 + "".join(["{s:^{w}}".format(s=x, w=10) for x in range(len(labels))]))
    
    for row in range(matrix.getHeight()):
        print("%8s %2d   " % (labels[row], row), end ="")
        
        print("".join(["{s:^{w}}".format(s=x, w=10) for x in matrix[row]]))
        

def traverseFromVertex(graph, startVertex, showProcess, collection = LinkedStack()):
    # Exercise
    structure = collection
    
    for vertex in graph.vertices():
        vertex.clearMark()
    
    structure.push(startVertex)

    while structure:
        poppedVertex = structure.pop()
        if not poppedVertex.isMarked():
            poppedVertex.setMark()
            if showProcess:
                print(poppedVertex)

            for vertex in poppedVertex.neighboringVertices():
                if not vertex.isMarked():
                    structure.push(vertex)
 
    
    

def depthFirstTraverse(graph, startVertex, showProcess):
    # Exercise
    traverseFromVertex(graph, startVertex, showProcess)


def breadthFirstTraverse(graph, startVertex, showProcess):
    # Exercise
    traverseFromVertex(graph, startVertex, showProcess, LinkedQueue())


    
def topoSort(graph):  
    # Exercise
    stack = LinkedStack()
    for vertex in graph.vertices():
        vertex.clearMark()

    for v in graph.vertices():
        if not v.isMarked():
            dfs(graph, v, stack)

    return stack

def dfs(graph, v, stack):
    v.setMark()
    for w in v.neighboringVertices():
        if not w.isMarked():
            dfs(graph, w, stack)

    stack.push(v)
        
    
          

def allPairsShortestPaths(matrix):
    # Exercise
    for i in range(0, matrix.getHeight()):
        for r in range(0, matrix.getHeight()):
            for c in range(0, matrix.getHeight()):
                matrix[r][c] = minWithInfinity(matrix[r][c], addWithInfinity(matrix[r][i], matrix[i][c]))
    

                
def dijkstra(graph, startVertex):
    # Extra Credit

    #Initialization
    included = []
    unincluded = []
    source = DijkstraEntry(startVertex)
    for vertex in graph.vertices():
        entry = DijkstraEntry(vertex)
        if vertex == startVertex:
            entry.distance = 0
            entry.path = None
            included.append(entry)

        elif startVertex.getEdgeTo(vertex):
            edge = startVertex.getEdgeTo(vertex)
            entry.distance = edge.getWeight()
            entry.path = startVertex.getLabel()
            unincluded.append(entry)

        else:
            entry.distance = INFINITY
            entry.path = None
            unincluded.append(entry)



    #Processing
    while unincluded:
        minDistance = unincluded[0].distance
        F = unincluded[0]
        for index in range(1, len(unincluded)):
            if unincluded[index] < F:
                F = unincluded[index]
        unincluded.remove(F)
        included.append(F)

        for T in unincluded:
            if T != F:
                edge = F.vertex.getEdgeTo(T.vertex)
                if edge:
                    newDistance = addWithInfinity(F.distance, edge.getWeight())
                    if lessThanWithInfinity(newDistance, T.distance):
                        T.distance = newDistance
                        T.path = F.vertex.getLabel()

    return included
                
                    
        

          
          
def main():
        
    # Create a directed graph using an adjacency list
    graph = LinkedDirectedGraph()
    
    # Add vertices with appropriate labels and print the graph
    graph.addVertex("A")
    graph.addVertex("B")
    graph.addVertex("C")
    graph.addVertex("D")
    graph.addVertex("E")
    graph.addVertex("F")
    graph.addVertex("G")
    graph.addVertex("H")
    graph.addVertex("I")
    graph.addVertex("J")
    # Insert vertices
    
    print("\nThe graph: \n" + str(graph))
    
    # Insert edges with weights and print the graph
    graph.addEdge("A", "J", 1)
    graph.addEdge("A", "I", 8)
    graph.addEdge("A", "B", 3)
    graph.addEdge("B", "C", 2)
    graph.addEdge("C", "E", 4)
    graph.addEdge("C", "G", 2)
    graph.addEdge("D", "I", 1)
    graph.addEdge("D", "B", 1)
    graph.addEdge("D", "C", 1)
    graph.addEdge("F", "C", 2)
    graph.addEdge("G", "D", 1)
    graph.addEdge("G", "F", 1)
    graph.addEdge("H", "B", 2)
    graph.addEdge("H", "E", 1)
    graph.addEdge("J", "B", 1)
    graph.addEdge("J", "H", 6)


    
    print("\nThe graph: \n" + str(graph))
    
    # Print the vertices adjacent to vertex A
    print("\nExpect vertices adjacent to A:")
    print(", ".join(list(map(str,graph.getVertex("A").neighboringVertices()))))
    
    # Print the edges incident to A
    print("Expect edges incident to A:")
    print(", ".join(list(map(str,graph.getVertex("A").incidentEdges()))))
    
    print("\nTraverse from vertex A:")
    traverseFromVertex(graph, graph.getVertex("A"), True)
    
    print("\nDepth first traversal:")
    depthFirstTraverse(graph, graph.getVertex("A"), True)
    
    print("\nBreadth first traversal:")
    breadthFirstTraverse(graph, graph.getVertex("A"), True)
    
    
        
    print("\nTopological sort:")
    stack = topoSort(graph)
    while not stack.isEmpty():
        print(stack.pop())
    
    
    print("\nLabel table for graph:")
    labelTable = makeLabelTable(graph)
    print(labelTable)
    
    
    print("\nInitial distance matrix for graph:")
    matrix = makeDistanceMatrix(graph, labelTable)
    printDistanceMatrix(matrix, labelTable)
    
    print("\nDistance matrix after running all pairs shortest paths:")
    allPairsShortestPaths(matrix)
    printDistanceMatrix(matrix, labelTable)
    
    try:
        print("\nExtra Credit, apply Dijkstra's algorithm from node A:\n")
            
        results = dijkstra(graph, graph.getVertex("A"))
        print("Node Distance Path Included")
        print("\n".join([str(results[x]) for x in range(len(results))]))
        
    except Exception as e:
        print("Extra Credit failed, error:", e)
        

if __name__ == '__main__':
    main()
