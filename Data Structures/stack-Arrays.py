class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.array = []
        self.length = 0
    
    def peek(self): # See top node
        return self.array[self.length-1] # Index of top stack will be length - 1 = top

    def push(self,value): # Add node to top 
        self.array.append(value) # Quick append the value we want
        self.length +=1
  

        
    def pop(self): # Remove from top
        popped_item = self.array[self.length-1] # Top index removed
        del self.array[self.length-1] # Delete using index
        self.length -= 1 
        return popped_item # Return the popped item

myStack = Stack() # Instantiate



print(myStack.push('google'))
print(myStack.push('udemy'))
print(myStack.push('discord'))
print(myStack.peek())
print(myStack.pop())
