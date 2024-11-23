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