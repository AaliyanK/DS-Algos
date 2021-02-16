# Creating linked list

# 10 --> 5 --> 16

# LinkedList = {
#     # first item is head
#     head: { # First node (dictionary) is container around data
#         value: 10,
#         next: { # Pointer to next node
#             value: 5,
#             next: {
#                 value:16,
#                 next: None # End of list
#             }
#         } 
#     }
# }

class newNode:
    def __init__(self,value):
        self.value=value
        self.next=None


class LinkedList:
    def __init__(self,value):
        self.head = {
            'value': value,
            'next': None
        }
        self.tail = self.head
        self.length = 1
    
    def append(self, value):
        newNode={
            'value': value,
            'next': None
        }
        self.tail['next']=newNode
        self.tail=newNode
        self.length=self.length+1
        return self
    
    def prepend(self,value):
        newNode={
            'value': value,
            'next': None
        }
        newNode['next']=self.head
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
            'next':None
        }
        leader = self.traverseToIndex(index-1) # The value BEFORE insert
        follower = leader['next'] # value after leader
        leader['next']=newNode
        newNode['next']=follower
        self.length+=1
        return self.printList()
    
    def remove(self,index): # O(n)
        leader = self.traverseToIndex(index-1)
        unwantedNode = leader['next']
        leader['next']=unwantedNode['next']
        self.length -=1
        return self.printList()
    
    def reverse(self): # Array = [1,10,16,88]
        prev = None
        while self.head:
            temp = self.head
            self.head = self.head['next']
            temp['next'] = prev
            prev = temp
        return prev



    








myLinked = LinkedList(10)

print(myLinked.append(16)) # Add to end of list -> NO LOOPING O(1)
print(myLinked.prepend(1)) # At beginning of linked list -> O(1)
print(myLinked.insert(2,99)) # In between indices -> O(n)
print(myLinked.head)
print(myLinked.tail)
print(myLinked.printList())
print(myLinked.insert(3,100))
print(myLinked.remove(2))

#INTERVIEW Q:

print(myLinked.reverse())