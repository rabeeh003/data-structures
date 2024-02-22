class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_ll(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.ref
    
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def insert(self, position, data):
        print(" position : ",position, ', data :',data)
        new_node = Node(data)
        run = 0
        n = self.head
        while run != position and n is not None:
            run += 1
            n = n.ref
        else:
            if run == position:
                new_node.ref = n.ref
                n.ref = new_node
            elif n == None:
                print('Invalid position !')
        
    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty ! ")
        else:
            self.head = self.head.ref
    
    def delete_end(self):
        if self.head is None:
            print("Linked list is empty ! ")
        else:
            n = self.head
            while n is not None:
                b = n.ref
                if b.ref is None:
                    n.ref = None
                    break
                else:
                    n = n.ref
    
    def delete_between(self, pos):
        if self.head is None:
            print('Linked list is empty!')
        else:
            n = self.head
            j = 0

            while j != pos-1 and pos != 0 and n is not None:
                j += 1
                n = n.ref

            if pos == 0:
                self.delete_begin()
            elif n is None:
                print('Invalid position!')
            else:
                n.ref = n.ref.ref
            


print("------ LinkedList --------")
print('Commands :\n 0. Print,\n 1. Add begin,\n 2. Add end,\n 3. Insert between,\n 4. Remove begin,\n 5. Remove end, \n 6. Remove between \n 10. Exit')
print("===========================")
new_node = LinkedList()
while True:
    choice = int(input("linkedList - $ "))
    if choice == 1:
        data = int(input("Enter the data : "))
        new_node.add_begin(data)
    elif choice == 2:
        data = int(input("Enter the data : "))
        new_node.add_end(data)
    elif choice == 3:
        position = int(input("Enter the position : "))
        data = int(input("Enter the data : "))
        new_node.insert(position-1, data)
    elif choice == 4:
        new_node.delete_begin()
    elif choice == 5:
        new_node.delete_end()
    elif choice == 6:
        pos = int(input("Enter position for delete : "))
        new_node.delete_between(pos)
    elif choice == 0:
        new_node.print_ll()
    elif choice == 10:
        break
    else:
        print("Invalid command.")
