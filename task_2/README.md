# COMP-2090SEF - Data Structures & Algorithms

A collection of Python implementations for data structures and algorithms coursework, featuring tree operations and sorting algorithms.

## 📋 Overview

This repository contains implementations of fundamental computer science concepts including:
- **Binary Tree Structures** - Node-based tree implementations
- **Heap Sort Algorithm** - Efficient in-place sorting technique
- **Tree Traversal & Manipulation** - Level-order insertion and tree operations

## 🗂️ Repository Structure

```
COMP-2090SEF/
├── task_1/              # First assignment
├── task_2/              # Second assignment
│   ├── binary tree.py   # Binary tree node implementation
│   ├── Heap sort.py     # Heap sort algorithm
│   └── mix of two.py    # Combined tree and heap sort implementation
├── goods.json           # Data file
└── README.md            # This file
```

## 📝 Task Descriptions

### Task 2: Trees & Sorting

#### `binary tree.py`
Implements a basic binary tree structure with node creation and manual tree construction:
- **Node Class**: Represents individual tree nodes with left/right children
- **Tree Setup**: Example tree with nodes containing character data (C, O, A, M, P, N)
- **Use Case**: Foundation for tree-based algorithms and data structure learning

#### `Heap sort.py`
Implements the complete heap sort algorithm:
- **heapify()**: Maintains the max-heap property by comparing parent with children
- **heapSort()**: Converts array into max-heap, then sorts by repeatedly extracting maximum
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(1) - in-place sorting
- **Example**: Sorts `[12, 11, 13, 5, 6, 7]` → `[5, 6, 7, 11, 12, 13]`

#### `mix of two.py`
Combines tree and sorting concepts:
- **SimpleTree Class**: Implements level-order (breadth-first) tree insertion
- **get_all()**: Returns all values in level-order traversal
- **Workflow**: 
  1. Create tree from unsorted values
  2. Extract values and sort using heap sort
  3. Create new tree from sorted values
- **Example**: Original `[7, 3, 9, 2, 5, 8, 1]` → Sorted `[1, 2, 3, 5, 7, 8, 9]` → New Tree

## 🚀 Usage

### Running Heap Sort
```bash
python task_2/Heap\ sort.py
```

Output:
```
Original array: [12, 11, 13, 5, 6, 7]
Arranged array: [5, 6, 7, 11, 12, 13]
```

### Running Combined Tree & Sort
```bash
python task_2/mix\ of\ two.py
```

Output:
```
==================================================
TREE → HEAP SORT → NEW TREE
==================================================
Original: [7, 3, 9, 2, 5, 8, 1]
Tree 1: [7, 3, 9, 2, 5, 8, 1]
Sorted: [1, 2, 3, 5, 7, 8, 9]
Tree 2 (from sorted): [1, 2, 3, 5, 7, 8, 9]

 Done! Tree values were sorted and made into a new tree.
```

## 🔑 Key Concepts

### Binary Trees
- Tree structure where each node has at most two children (left and right)
- Building block for many advanced data structures (BSTs, AVL trees, etc.)

### Heap Sort
- Comparison-based sorting algorithm with guaranteed O(n log n) performance
- Uses heap data structure (complete binary tree with heap property)
- Better worst-case than quicksort; more efficient than insertion sort for large datasets

### Tree Traversal
- **Level-Order (BFS)**: Visit nodes level by level from top to bottom
- Used in `SimpleTree.insert()` to maintain complete binary tree property

## 💻 Language

- **Python 3.x**

## 📚 Learning Outcomes

By studying this code, you will understand:
- ✅ How to implement basic tree structures
- ✅ Heap properties and heap-based sorting
- ✅ In-place sorting techniques
- ✅ Tree traversal algorithms
- ✅ Time and space complexity analysis

## 📌 Notes

- All implementations are educational and emphasize clarity over optimization
- Binary tree values use character and numeric data types
- Heap sort is stable when combined with proper tree reconstruction

---

**Course**: COMP-2090SEF  
**Created**: 2026  
**Language**: Python