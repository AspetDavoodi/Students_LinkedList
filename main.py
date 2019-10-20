class Node:

    def __init__(self, data1=None, data2=None, next_node=None):
        self.data1 = data1
        self.data2 = data2
        self.next_node = next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def insert(self, data1, data2):
        new_node = Node(data1, data2)
        new_node.set_next(self.head)
        self.head = new_node

    def display(self):
        printval = self.head
        while printval is not None:
            print (printval.data1, printval.data2)
            printval = printval.next_node

        print ("--------------------")


def main():

    Students = LinkedList()

    Students.insert("A", 4)
    Students.insert("B", 3)
    Students.insert("C", 3.5)
    Students.insert("D", 3.8)

    Students.display()

main()

