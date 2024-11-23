# Colab
Colab link for [**Algorithm**](https://colab.research.google.com/drive/1EK4-z03QZUcAFj4SC2gbSqdx1KCDb22m?usp=sharing) and [**Data Structure**](https://colab.research.google.com/drive/1ypTLTR4JWhNfyrh9RRoMk7dXtyoM_zFz?usp=sharing)

# Algorithms

## Searching

### Linear Search - Basic Loops
Sequentially Checks each element in a list

* Time Complexity: 𝑂(n)
* Space Complexity: 𝑂(1) - iterative, in-place search.

```
def linearSearch(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
        return i
    return -1 # target not found
```
#### Steps
1. Start from the first element of the array
2. Compare the current element with the target element
3. If they match, return the index of the current element.
4. If not, move to the next element.
5. Repeat steps 2-4 until the target element is found or reaching the end of the array.

#### Advantages
* Unsorted data
* Simple to implement

#### Disadvantages
* Inefficient for large datasets

#### Applications
* Unsorted Datasets.
* Useful for small datasets.
* Searching in Linked Lists or Streams.

### Binary Search - Sorted List, faster
Works on sorted lists by dividing the search range in half.
* Time Complexity: 𝑂(log n)
* Space Complexity: 𝑂(1) for iterative, 𝑂(log n) if recursive due to function call stack.
* Limitations: Sorted input Array

```
def binarySearch_IterativeApproach(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high)//2
        if array[mid] == target:
            return mid 
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1 # Target not found


def binarySearch_RecursiveApproach(array, target, low, high):
    if low > high:
        return -1 # Target not found
  
    mid = (low + high) // 2

    if array[mid] == target:
        return mid 
    elif array[mid] < target:
        return binarySearch_RecursiveApproach(array, target, mid+1, high)
    else:
        return binarySearch_RecursiveApproach(array, target, low, mid-1)
```
#### Steps
1. Start with 2 pointers: `low` (begining of the array) and `high` (end of the array)
2. Calculate the `mid` index:`mid` = ⌊(`low` + `high`)/2⌋
3. Compare the target element with the element at the `mid` index
  * If equal, return `mid`
  * If smaller, adjust `high` to `mid-1`
  * If larger, adjust `low` to `mid+1`
4. Repeat steps 2-3 until `low` exceeds `high` or the element is found
5. If the element is not found, return `-1`

#### Approaches
1. Iterative Approach - suitable for applications where recursion depth might be an issue.
2. Recursive Approach - Elegant and concise, but extra space used on call stack for each recursive call.

### [Breadth First Search - Shortest Path (unweighted graph)](https://leetcode.com/problem-list/breadth-first-search/)
Explores **all nodes** at the current depth level before moving to the next level.
It uses a queue data structure to keep track of nodes to visit.
* Time Complexity: 𝑂(𝑉 + 𝐸), where
  - 𝑉 is the number of vertices and
  - 𝐸 is the number of edges.
* Space Complexity: 𝑂(𝑉) for the queue and visited set.

```
from collections import deque 
def bfs(graph, start):  
    visited = set() # To keep track on visited nodes
    queue = deque([start]) # Initialize the queue with the start node
    visited.add(start)

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```
#### Steps
1. Start with the initial node and mark it as visited.
2. Add the source node to a queue.
3. While the queue is not empty:
  * Remove the front node from the queue.
  * Visit all its neighbors that have not been visited and add them to the queue.
4. Repeat until all nodes at all levels are visited or the tarrget node is found.

#### Advantages
* Finds the shortest path in unweighted graphs.

#### Disadvantages
* Consume significant memory for large graphs.

#### Applications
* [Shortest Path in Unweighted Graphs](#scrollTo=qJQdMkkl9rN-&line=1&uniqifier=1) - shortest path between 2 nodes.
* Level Order Traversal in Trees - traverse a tree level by level.
* Connected Components - determining connected components of a graph.
* Cycle Detection - detects cycles in undirected graphs.
* Web Crawlers - explores pages level by level in a web graph.

#### Promises
* Explores **All Nodes** at current distance from the source before moving to nodes at a greater distance.
* Process nodes in **The Order they are Discovered**. When a node is first visited, it is reached via the shortest possible path.