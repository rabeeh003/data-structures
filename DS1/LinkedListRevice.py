class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class linkedList:
    def __init__(self):
        self.head = None
    
    def add_data(self,data):
        node = Node(data)
        node.ref = self.head
        self.head = node

    def print_data(self):
        if self.head is None:
            print("linked list is none \n")
        else:
            next_node = self.head
            while next_node is not None:
                print(next_node.data)
                next_node = next_node.ref

    def revise_data(self):
        current = self.head
        priv = None
        while current is not None:
            nex = current.ref
            current.ref = priv
            priv = current
            current = nex
        self.head = priv

my_list = linkedList()
my_list.add_data(3)
my_list.add_data(5)
my_list.add_data(7)

print("Original Linked List:")
my_list.print_data()

my_list.revise_data()
print("Reversed Linked List:")
my_list.print_data() 