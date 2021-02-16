# Edge List
graph1 = [[0,2], [2,3], [2,1], [1,3]]

# Adjacent List
graph2 = [[2], [2,3], [0,1,3],[1,2]]

# Adjacent Matrix
graph3 = {
    '0': [0,0,1,0],
    '1': [0,0,1,1],
    '2': [1,1,0,1],
    '3': [0,1,1,0]
}

# Implementation:

class Graph:
    def __init__(self):
        self.numOfNodes = 0
        self.adjacentList = {}
    
    def addVertex(self, node):
        # Set dictionary '0':[] for now
        self.adjacentList[node] = [] # No edges/connections yet
        self.numOfNodes += 1

    def addEdge(self,node1,node2):
        # Undirected Graph -> Back and forth
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)

    def showConnects(self):
        for x in self.adjacentList:
            print(x , end = '-->')
            for i in self.adjacentList[x]:
                print(i , end = ' ') 
            print()

myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('3', '1')
myGraph.addEdge('3', '4')
myGraph.addEdge('4', '2') 
myGraph.addEdge('4', '5') 
myGraph.addEdge('1', '2') 
myGraph.addEdge('1', '0') 
myGraph.addEdge('0', '2') 
myGraph.addEdge('6', '5')
print(myGraph)
myGraph.showConnects()