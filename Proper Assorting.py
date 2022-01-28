class linkedListNode:
    def __init__(self, value, nextNode = None): #setting nextNode = None allows us to manually adjust value seperate of the called class input values
        self.value = value
        self.nextNode = nextNode

# simple declaring of nodes to linkedListNode class
node1 = linkedListNode('3')
node2 = linkedListNode('2')
node3 = linkedListNode('4')

#simple adding of nodes to linkedlist
node1.nextNode = node2
node2.nextNode = node3


currentNode = node1
while True:
    print (currentNode.value, "->"),
    if currentNode.nextNode is None: 
        print ("None")
        break
    currentNode = currentNode.nextNode
    
# alternate way of doing this

class linkedListNode:
    def __init__(self, value, nextNode = None): #setting nextNode = None allows us to manually adjust value seperate of the called class input values
        self.value = value
        self.nextNode = nextNode

class linkedList: #only keeps track of the head node
    def __init__(self, head = None):
        self.head = head
    
    def insert(self, value): 
        node = linkedListNode(value) # this value called from the fist class allows us to use user input
        if self.head is None: # checks to verify if their are any nodes in the list
            self.head = node
            return
        currentNode = self.head
        while True:
            if currentNode.nextNode is None: # checks to see if there is more than one node
                currentNode.nextNode = node # if there is no next node but we have a first node, our user input allows us to add the user input as the new next node
    
    def printlinkedList(self):
        currentNode = self.head
        while currentNode.value is not None:
            print (currentNode.value, "->")
            currentNode = currentNode.nextNode
            