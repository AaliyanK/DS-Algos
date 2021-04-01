class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return
        temp = self.root
        while True:
            if new_node.value < temp.value:
                if temp.left == None:
                    temp.left = new_node
                    break
                else:
                    temp = temp.left
            elif new_node.value > temp.value:
                if temp.right == None:
                    temp.right = new_node
                    break
                else:
                    temp = temp.right

    def lookup(self, value):
        temp = self.root
        while True:
            if temp.value == value:
                return True
            elif temp == None:
                return False
            elif value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right

    def breadthFirstSearch(self):
        currentNode = self.root
        finalList = []
        queue = []  # Keep track of level to access children
        queue.append(currentNode)
        
        while len(queue) > 0:
            currentNode = queue[0] # Memory consumption happens here, the queue gets added here
            del queue[0]
            print(currentNode.value)
            finalList.append(currentNode.value) # Add 9 here
            if currentNode.left:
                queue.append(currentNode.left) # Add 4 to queue
            if currentNode.right:
                queue.append(currentNode.right) # Add 20 to queue
        return finalList
    
    def breadthFirstSearchRecursive(self, queue, mylist):
        if len(queue) == 0:
            return mylist
        currentNode = queue[0]
        del queue[0]
        mylist.append(currentNode.value) 
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
        return self.breadthFirstSearchRecursive(queue, mylist)
    
    def DFSInOrder(self, currnode, mylist): # DFS usually done with recursion
        if currnode != None:
            self.DFSInOrder(currnode.left,mylist)
            mylist.append(currnode.val)
            self.DFSInOrder(currnode.right,mylist)
        return mylist

    def DFSPostOrder(self, currnode, mylist):
        if currnode.left:
            self.DFSPostOrder(currnode.left,mylist)
        if currnode.right:
            self.DFSPostOrder(currnode.right,mylist)
        mylist.append(currnode.val)
        return mylist

    def DFSPreOrder(self, currnode, mylist):
        if currnode!=None:
            mylist.append(currnode.val)
            self.DFSPreOrder(currnode.left,mylist)
            self.DFSPreOrder(currnode.right,mylist)
        return mylist

#          9
#      4       20
#    1    6  15    170  


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.breadthFirstSearch()
tree.breadthFirstSearchRecursive([tree.root],[])
print(tree.DFSInOrder(tree.root,[]))
print(tree.DFSPostOrder(tree.root,[]))
print(tree.DFSPreOrder(tree.root,[]))