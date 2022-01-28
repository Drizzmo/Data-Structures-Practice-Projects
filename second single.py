
class Node:
    def __init__(self, data=None):
        self.data = data 
        self.next = None # next node action for method defined
        
class singly_linked_list: # define linked list class that creates iterating objects; creates an empty list for data input
    def __init__(self):
        self.head = None #define our head node for the beginning of our list
        self.tail = None #define tail as last node in the list
        self.count = 0 # provides current index of tail
    
    def iterate_item(self): # dont need anything beyond self because we are not adding or subtracting from the list
        current_item = self.head
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val # use yield when we want to produce a sequence of values
            
    def append_item(self, data):
        node = Node(data) # pulls the data parameter from the original method from above
        if self.tail:
            self.tail.next = node # dont understand this
            self.tail = node # dont understand this
        else:
            self.head = node # dont understand this
            self.tail = node # dont understand this
        self.count += 1
items = singly_linked_list()
items.append_item('data')
items.append_item('set')
items.append_item('is')
items.append_item('added')

for val in items.iterate_item():
    print(val)
print("\nhead.data: ", items.head.data)
print("\ntail.data: ", items.tail.data)