class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

firstNode = Node("C")
secondNode = Node("O")
thirdNode = Node("A")
fourthNode = Node("M")
fifthNode=Node("P")
sixthNode=Node("N")


firstNode.left=secondNode
firstNode.right=thirdNode
secondNode.left=fourthNode
secondNode.right=fifthNode
thirdNode.left=sixthNode
