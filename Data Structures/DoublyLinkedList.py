class doubleLinkedList:
    def __init__(self,value):
        self.head = {
            'value': value,
            'next': None,
            'prev': None
        }
        self.tail = self.head
        self.length = 1
    
    def append(self, value):
        newNode={
            'value': value,
            'next': None,
            'prev': None # THIS!!
        }
        newNode['prev'] = self.tail
        self.tail['next']=newNode
        self.tail=newNode
        self.length=self.length+1
        return self
    
    def prepend(self,value):
        newNode={
            'value': value,
            'next': None,
            'prev':None
        }
        newNode['next']=self.head
        self.head['prev'] = newNode
        self.head=newNode
        self.length = self.length +1
        return self
    
    def printList(self):
        array = []
        currentNode=self.head
        while currentNode != None:
            array.append(currentNode['value'])
            currentNode = currentNode['next']
        return array

    def traverseToIndex(self, index): #Lookup -> O(n)
        counter = 0
        currentNode = self.head #Starts at first node
        while counter != index: 
            currentNode = currentNode['next']
            counter+=1
        return currentNode

    def insert(self,index,value): # What index we want to insert into
        # Check params
        if index >= self.length: # If input index is greater than list size, just add to end
            return self.append(value)
     
        newNode = {
            'value': value,
            'next':None,
            'prev': None
        }
        leader = self.traverseToIndex(index-1) # The value BEFORE insert
        follower = leader['next'] # value after leader
        leader['next']=newNode
        newNode['prev'] = leader
        newNode['next']=follower
        follower['prev']=newNode
        self.length+=1
        return self.printList()
    
    def remove(self,index): # O(n)
        leader = self.traverseToIndex(index-1)
        unwantedNode = leader['next']
        leader['next']=unwantedNode['next']
        self.length -=1
        return self.printList()

    








myLinked = doubleLinkedList(10)

print(myLinked.append(16)) # Add to end of list -> NO LOOPING O(1)
print(myLinked.append(5))
print(myLinked.printList())
print(myLinked.prepend(1)) # At beginning of linked list -> O(1)
print(myLinked.printList())
# print(myLinked.insert(2,99)) # In between indices -> O(n)
# print(myLinked.head)
# print(myLinked.tail)
# print(myLinked.printList())
# print(myLinked.insert(3,100))
# print(myLinked.remove(2))