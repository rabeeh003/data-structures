class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class Binary_tree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._ins(self.root, data)

    def _ins(self, node, data):
        if node is None:
            return Node(data)
        else:
            if data < node.data:
                node.left = self._ins(node.left, data)
            else:
                node.right = self._ins(node.right, data)
        return node
    
    def inOrder_traversal(self):
        self._inOrder(self.root)
    
    def _inOrder(self, node):
        if node:
            self._inOrder(node.left)
            print(node.data,"  ")
            self._inOrder(node.right)
    
bt = Binary_tree()
bt.insert(100)
bt.insert(80)
bt.insert(70)
bt.insert(90)
bt.insert(110)
bt.insert(105)
bt.insert(115)

bt.inOrder_traversal()