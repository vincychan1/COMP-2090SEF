class Node: 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self, root_value=None):
        if root_value!=None:
            self.root=Node(root_value)
        else:
            self.root=None
    
    def is_empty(self):
        return self.root==None
    
    def height(self, node=None):
        if node==None:
            node = self.root 
        if node==None:
            return 0  
        left_height=self.height(node.left)
        right_height=self.height(node.right)
        
        return max(left_height, right_height) + 1
    
    def size(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)
