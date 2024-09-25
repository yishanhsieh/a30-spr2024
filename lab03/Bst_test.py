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

# a = BstNode(3)
# a.left = BstNode(5)
# a.left.right = BstNode(1)
# a.display()

# print("------------")
# b = BstNode(7)
# b.left = BstNode(4)
# a.right = b
# a.display()

# print("------------")
# b = BstNode(2)
# b.right = a.right
# a.right = b
# a.display()


def find_largest(bst):
    if bst.right == None:
        return bst.key
    else:
        return find_largest(bst.right)


class BST(BstNode):
    def __init__(self, name):
        super().__init__(name)

    def insert(self, value):
        if self.key == value:
            return
        elif self.key < value:
            if self.right == None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        else:
            if self.left == None:
                self.left = BST(value)
            else:
                self.left.insert(value)

    def find(self, value):
        if self.key == value:
            return True
        elif self.key < value:
            if self.right == None:
                return False
            else:
                return self.right.find(value)
        else:
            if self.left == None:
                return False
            else:
                return self.left.find(value)

    def remove(self,value):
        if self.key == value:
            if self.right == None:
                return self.left
            if self.left == None:
                return self.right
            else:  #if have >=2 children
                num = find_largest(self.left)
                self.key = num
                self.left = self.left.remove(num)
        elif self.key < value:
            self.right = self.right.remove(value)
        else:
            self.left = self.left.remove(value)
        return self


        

a = BST(8)
for num in [1,9,7,2,6,4,5]:
    a.insert(num)
print("Consider this tree:")
a.display()
print("If I remove the root:")
a = a.remove(8)
a.display()
