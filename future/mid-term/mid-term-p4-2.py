# Mid-term P4-2
# Then consider the template provided for BST (shown above, on the right). Write code for a class 
# that implements a BST ADT starting from BstNode (via the class extension mechanism, as shown 
# and as demonstrated in class) with the following three operations: find, insert and remove. Give 
# some examples of how your BST ADT code runs (to test your BST class implementation). 


from BstNode import BstNode

class BST(BstNode):
    def __init__(self, name):
        super().__init__(name)
    def insert(self, value):
        a = BST(value)
        a.right = self.right
        self.right = a


        