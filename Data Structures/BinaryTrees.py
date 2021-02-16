class Node:
  def __init__(self,value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        newNode = Node(value) # Create new Node
        if self.root == None: # If not root node, make that our top
            self.root = newNode
            return print(f'{newNode.value} Is ROOT node')
        else:
            currentNode = self.root # A placeholder
            while True:
                if value < currentNode.value:
                    # we want to go LEFT
                    if currentNode.left == None: # Only if there is nothing in the left node, we have a spot
                        currentNode.left = newNode
                        return print(f'{newNode.value} Moves to RIGHT')
                    else:
                        currentNode = currentNode.left # Otherwise, redo the loop 
                elif value > currentNode.value:
                    # We want to go RIGHT
                    if currentNode.right == None: # Only if there is nothing in the right
                        currentNode.right = newNode
                        return print(f'{newNode.value} Moves to LEFT')
                    else:
                        currentNode = currentNode.right # Otherwise, redo the loop

        

    def lookup(self,value):
        if self.root is None:
            return False # If root doesnt exist, no nodes will be present
        curr_node = self.root # Starting at top node
        while curr_node: # While true:
            if value < curr_node.value: # Traverse left
                curr_node = curr_node.left 
            elif value > curr_node.value: # Traverse right
                curr_node = curr_node.right
            elif curr_node.value == value: # When we find our lookup value, return it
                return curr_node.value, curr_node.left.value, curr_node.right.value
            return False

# TO GET THE TREE BACK
    def print_tree(self):
        if self.root != None:
            self.printt(self.root)

    def printt(self,curr_node):
        if curr_node != None:
            self.printt(curr_node.left)
            print(str(curr_node.value))
            self.printt(curr_node.right)
    

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
print(tree.lookup(170))
