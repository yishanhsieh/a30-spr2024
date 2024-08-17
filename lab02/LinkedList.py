#linkedData
# what is linkedlist? https://www.geeksforgeeks.org/what-is-linked-list/


class LinkedList:
    def __init__(self, num, next):
        self.num = num
        self.next = next

    def show(self):
        temp = self
        result = ''
        while (temp):  #while temp has value
            result = result + '--> ' + temp.num + '--> '
            temp = temp.next
        print(result)

def main():
    print("==========Class LinkedList===========")
    a = LinkedList("Christa", None)
    print("Starting with empty list we add Christa: ", end='')
    a.show()
    a = LinkedList("Ahmed", a) 
    print("Adding Ahmed we get: ", end='')
    a.show()
    a = LinkedList("Leslie", a) 
    print("Then we add Leslie.")
    a = LinkedList("Larry", a) 
    print("Then Larry.")
    a = LinkedList("Laura", a) 
    print("Finally we add Laura.")
    print("Our list now: ", end='')
    a.show()

if __name__ == "__main__":
    main()