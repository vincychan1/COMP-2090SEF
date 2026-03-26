class Node: 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self, root_value=None):
        if root_value is not None:
            self.root=Node(root_value)
        else:
            self.root=None
    
    def is_empty(self):
        return self.root is None
    
    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))
    
    def height(self): 
        if self.root is None:
            return 0
        return self._height(self.root)
    
    def _size(self, node):
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)
    
    def size(self):
        if self.root is None:
            return 0
        return self._size(self.root)
    
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)

print(f"Is tree empty? {tree.is_empty()}")
print(f"Tree height: {tree.height()}")
print(f"Tree size: {tree.size()}")
