# Binary Search Tree

# NO ONE TOUCHES THIS CLASS. ITS JUST USED TO CALL AND IDENTIFY THIS DATA
class node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None

class binary_search_tree:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        if self.root==None:
            self.root==node(value)
        else: 
            self._insert(value, self.root) # _ symbol makes sure people know that this function is private and shouldnt be called outside this class
            
    # recursive function that allows us to place data into the tree correctly
    def _insert(self,value,cur_node):
        if value<cur_node.value:
            if cur_node.left_child==None:
                cur_node.left_child==node(value)
            else:
                self._insert(value,cur_node.left_child)
        elif value>cur_node.value: # checks for greater than value 
            if cur_node.right_child==None:
                cur_node.right_child==node(value)
            else:
                self._insert(value,cur_node.right_child)
        else:
            print("Value already in tree!")
    
    def print_tree(self):
        if self.root!=None:
            self._print_tree(self.root)
    
    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print str(cur_node.value)
            self._print_tree(cur_node.right_child)

def fill_tree

tree = binary_search_tree()
