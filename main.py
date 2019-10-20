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

    def displayGoodStudents(self):
        printval = self.head
        while printval is not None:
            if printval.data2 > 3.4:
                print (printval.data1)
                printval = printval.next_node
            else:
                printval = printval.next_node


def main():

    Students = LinkedList()

    Students.insert("A", 4)
    Students.insert("B", 3)
    Students.insert("C", 3.3)
    Students.insert("D", 3.6)
    Students.insert("E", 3.67)
    Students.insert("F", 3.89)
    Students.insert("G", 3.45)

    # Students.display()

    Students.displayGoodStudents()

main()

