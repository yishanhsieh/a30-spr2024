#binary tree
class BinaryTree:
    def __init__(self, value, left, right) -> None:
        self.value = value
        self.left = left
        self.right = right

    def show(self):
        if self.left == None:
            left = ' . '
        else:
            left= self.left.show()

        if self.right == None:
            right = ' . '
        else:
            right = self.right.show()

        return "(" + left + " "+ str(self.value) + " " + right + ")"


def main():
    print("---------------------------Class BinaryTree---------------------------")
    a = BinaryTree(4, None, None)
    a = BinaryTree(6, a, BinaryTree(7, None, None))
    a = BinaryTree(3, BinaryTree(1, None, None), a)
    a = BinaryTree(8, a, BinaryTree(10, None, BinaryTree(14, BinaryTree(13, None, None),None)))
    print(a.show())

if __name__ == "__main__":
    main()