class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None # Top plate
        self.bottom = None
        self.length = 0 
    
    def peek(self): # See top node
        return self.top.value

    def push(self,value): # Add node to top 
        newNode = Node(value) # Add new node for new item
        if (self.length == 0): # If length is 0, then top and bottom will be the same
            self.top = newNode
            self.bottom = newNode
        else:
            holdingPointer = self.top
            self.top = newNode
            self.top.next = holdingPointer
        self.length +=1
  

        
    def pop(self): # Remove from top
        if self.top is None:
            return None
        pointer = self.top
        self.top=self.top.next
        return pointer.value # Will return top of stack (discord)

myStack = Stack() # Instantiate



print(myStack.push('google'))
print(myStack.push('udemy'))
print(myStack.push('discord'))
print(myStack.peek())
print(myStack.pop())
