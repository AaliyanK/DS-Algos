class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None # Top plate
        self.last = None
        self.length = 0 
    
    def peek(self): # See first item
        return self.first.value


    def enqueue(self,value): # Add to PERSON TO LINE (BACK OF LINE)
        new_node = Node(value) # Has self.value and self.next
        if self.length == 0: # If no people in line, then:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node # Should be None, cuz no one behind the last person, but now new person will be the last
            self.last = new_node # Make new person in line the last person
        self.length+=1
        return self.first.value, self.last.value, self.length
        

    def dequeue(self): # remove from front of line (Let first person in line, into event)
        if self.first is None: # IF NO PERSON IN LINE
            return None
        if self.first == self.last: # If one person in line only
            self.last = None
        self.first = self.first.next 
        self.length -= 1
        return self.first.value, self.last.value, self.length


myQueue = Queue() # Instantiate

print(myQueue.enqueue('Joy'))
print(myQueue.enqueue('Matt'))
print(myQueue.enqueue('Pavel'))
print(myQueue.enqueue('Samir'))
print(myQueue.dequeue())
print(myQueue.peek())