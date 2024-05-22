class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._ins(self.root, data)
    def _ins(self,node,data):
        if node is None:
            node.data = data
            return
        else:     
            if node.data > data:
                self._ins(node.left, data)
            else:
                self._ins(node.right, data)
        return node
    
    
    