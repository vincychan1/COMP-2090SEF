# COMP-2090SEF - Data Structures & Algorithms

A collection of Python implementations for data structures and algorithms coursework, featuring binary tree and heap sort.

video link: https://youtu.be/0KdcwHQn_uo 

## 📋 Overview

This repository contains implementations of fundamental computer science concepts including:
- **Binary Tree Structures** - Node-based tree implementations
- **Heap Sort Algorithm** - Efficient in-place sorting technique
- **Binary Tree + Heap Sort** - Level-order insertion and tree operations

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


## 🔑 Key Concepts

### Binary Trees
- Tree structure where each node has at most two children (left and right)
- Building block for many advanced data structures (BSTs, AVL trees, etc.)

### Heap Sort
- Comparison-based sorting algorithm with guaranteed O(n log n) performance
- Uses heap data structure (complete binary tree with heap property)
- Better worst-case than quicksort; more efficient than insertion sort for large datasets
