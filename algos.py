from collections import deque
from node_pieces import *

"""Breadth First Search
    Basic steps:
        We work Level by level (Depth) to find a solution
        We use a queue to get through each level, pushing the new nodes from the back
        and popping from the front ensuring we work through each level fully before moving on (FIFO)
    Solution involves finding the the shortest number of actions to complete path
"""
def bfs(grid, start, end):
    queue = deque()
    start_node = Node(start)
    queue.append(start_node)
    
    closed = set()
    
    while queue:
        current = queue.popleft()
        
        if current.position in closed:
            continue
        closed.add(current.position)
        
        if current.position == end:
            path = retrace_path(current)
            open_list = {node.position for node in queue}
            return path, closed, open_list
        
        for neighbor_pos in get_neighbors(grid, current.position):
            if neighbor_pos not in closed:
                neighbor_node = Node(neighbor_pos, parent=current)
                queue.append(neighbor_node)
    
    return None, closed, set()  # no path found

"""Uniform Cost Search
    
"""