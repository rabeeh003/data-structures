# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.children = []

#     def add_child(self, child):
#         self.children.append(child)
    
# def print_tree(root, level=0):
#     if root:
#         print("  " * level + str(root.data))
#         for child in root.children:
#             print_tree(child, level + 1)

# root = Node("A")
# b = Node("B")
# c = Node("C")
# d = Node("D")
# e = Node("E")
# f = Node("F")
# g = Node("G")
# h = Node("H")

# root.add_child(b)
# root.add_child(c)
# b.add_child(d)
# b.add_child(e)
# c.add_child(f)
# c.add_child(g)
# g.add_child(h)

# print("Tree structure:")
# print_tree(root)


# ----------------
# tree example
class Node:
    def __init__(self, data):
        self.data = data
        self.child = []
    
    def add_child(self, child):
        self.child.append(child)
    
def print_child(root):
    if root:
        print(root.data)
        for child in root.child:
            print_child(child)

root = Node(1)

c1 = Node(20)
c2 = Node(30)
c3 = Node(40)

c4 = Node(500)
c5 = Node(600)
c6 = Node(700)

# _____
root.add_child(c1)
root.add_child(c2)
root.add_child(c3)

c1.add_child(c4)
c1.add_child(c5)
c4.add_child(c6)


print_child(root)