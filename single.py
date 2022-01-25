#create a single linked list that iterates through the list starting at the head node.
#should also be able to append items
# GET AND SET FOR EACH NODE
#define the node class
class Node:
    # define __init__ constructor to allow for calling of attributes for objects
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    # define set next node method to allow for adding to list iteration
    # this is an action method that actually changes the iteration
    def set_next_node(self, next_node):
        self.next_node = next_node

    # define get next node to call this value
    # this is a call method that just calls a value
    def get_next_node(self):
        return self.next_node
    
    # define get value to call the value of the node
    # this is a call method that just calls the value
    def get_value(self):
        return self.value
 
 # define a class to create the linked list and the actions to iterate/add to the list
class linked_list:
    # define __init__ constructor to allow for calling of object attributes
    def __init__(self, value=None):
        self.head_node = Node(value) 
    
    #now we need to call our head node; no need to set next node because its been done for us
    def get_head_node(self):
        return self.head_node
