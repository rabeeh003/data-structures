class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insertion(self.root, data)
        
    def _insertion(self, node, data):
        if node is None:
            return Node(data)
        else:
            if node.data > data:
                node.left = self._insertion(node.left, data)
            else:
                node.right = self._insertion(node.right, data)
        return node
    
    def inOrder(self):
        self._inOrder(self.root)
    
    def _inOrder(self,node):
        if node:
            self._inOrder(node.left)
            print(node.data, " ")
            self._inOrder(node.right)
        
bt = BST()
bt.insert(100)
bt.insert(80)
bt.insert(70)
bt.insert(90)
bt.insert(110)
bt.insert(105)
bt.insert(115)

bt.inOrder()