class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class SimpleTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        
        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            if not curr.left:
                curr.left = Node(value)
                return
            if not curr.right:
                curr.right = Node(value)
                return
            queue.append(curr.left)
            queue.append(curr.right)
    
    def get_all(self):
        values = []
        if self.root:
            queue = [self.root]
            while queue:
                curr = queue.pop(0)
                values.append(curr.value)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return values

def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

# Tree values -> Sort -> New tree
print("="*50)
print("TREE → HEAP SORT → NEW TREE")
print("="*50)

# Original numbers
numbers = [7, 3, 9, 2, 5, 8, 1]
print(f"Original: {numbers}")

# Make a tree
tree1 = SimpleTree()
for n in numbers:
    tree1.insert(n)
print(f"Tree 1: {tree1.get_all()}")

# Sort tree values using heap sort
sorted_vals = heap_sort(tree1.get_all().copy())
print(f"Sorted: {sorted_vals}")

# Make new tree from sorted values
tree2 = SimpleTree()
for n in sorted_vals:
    tree2.insert(n)
print(f"Tree 2 (from sorted): {tree2.get_all()}")

print("\n Done! Tree values were sorted and made into a new tree.")
