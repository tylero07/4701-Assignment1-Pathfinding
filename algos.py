import heapq
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
        Will pick the cheapest route and only keep the cheapest
        Will weigh all options and choose the cheapest
        Continue Path until a solution is found
        Will order the Solutions keeping only the cheapest
"""
def ucs(grid, start, end):
    start_node = Node(start, cost=0)
    open_queue = []
    heapq.heappush(open_queue, start_node)
    
    closed = set()
    
    while open_queue:
        current = heapq.heappop(open_queue)
        
        if current.position in closed:
            continue
        closed.add(current.position)
        
        if current.position == end:
            path = retrace_path(current)
            open_list = {node.position for node in open_queue}
            return path, closed, open_list, current.cost
        
        for neighbor_pos in get_neighbors(grid, current.position):
            if neighbor_pos not in closed:
                new_cost = current.cost + COSTS[grid[neighbor_pos[0]][neighbor_pos[1]]]
                neighbor_node = Node(neighbor_pos, parent=current, cost=new_cost)
                heapq.heappush(open_queue, neighbor_node)
    
    return None, closed, set()

"""Manhattan heuristic
    uses the shortest grid distance from start to finish to find 
    a good "Price is right" guess"""
def manhattan(pos, end):
    return abs(pos[0] - end[0]) + abs(pos[1] - end[1])

def euclidean(pos, end):
    return ((pos[0] - end[0])**2 + (pos[1] - end[1])**2) ** 0.5

"""Greedy Best-First Search
    Uses Heuristic (guess) to find the shortest path w/o worrying about cost or alternates
    
    """
def greedy(grid, start, end):
    start_node = Node(start, cost=0)
    open_queue = []
    heapq.heappush(open_queue, (manhattan(start, end), start_node))
    
    closed = set()
    
    while open_queue:
        _, current = heapq.heappop(open_queue)
        
        if current.position in closed:
            continue
        closed.add(current.position)
        
        if current.position == end:      
            path = retrace_path(current)
            open_list = {node.position for _, node in open_queue}
            return path, closed, open_list, current.cost
                
        for neighbor_pos in get_neighbors(grid, current.position):
            if neighbor_pos not in closed:
                new_cost = current.cost + COSTS[grid[neighbor_pos[0]][neighbor_pos[1]]]
                neighbor_node = Node(neighbor_pos, parent=current, cost=new_cost)
                h = manhattan(neighbor_pos, end)
                heapq.heappush(open_queue, (h, neighbor_node))
    
    return None, closed, set()

def astar_manhattan(grid, start, end):
    start_node = Node(start, cost=0)
    open_queue = []
    heapq.heappush(open_queue, (manhattan(start, end), start_node))
    
    closed = set()
    
    while open_queue:
        _, current = heapq.heappop(open_queue)
        
        if current.position in closed:
            continue
        closed.add(current.position)
        
        if current.position == end:
            path = retrace_path(current)
            open_list = {node.position for _, node in open_queue}
            return path, closed, open_list, current.cost
        
        for neighbor_pos in get_neighbors(grid, current.position):
            if neighbor_pos not in closed:
                new_cost = current.cost + COSTS[grid[neighbor_pos[0]][neighbor_pos[1]]]
                neighbor_node = Node(neighbor_pos, parent=current, cost=new_cost)
                f = new_cost + manhattan(neighbor_pos, end)
                heapq.heappush(open_queue, (f, neighbor_node))
    
    return None, closed, set(), 0

def astar_euclidean(grid, start, end):
    start_node = Node(start, cost=0)
    open_queue = []
    heapq.heappush(open_queue, (euclidean(start, end), start_node))
    
    closed = set()
    
    while open_queue:
        _, current = heapq.heappop(open_queue)
        
        if current.position in closed:
            continue
        closed.add(current.position)
        
        if current.position == end:
            path = retrace_path(current)
            open_list = {node.position for _, node in open_queue}
            return path, closed, open_list, current.cost
        
        for neighbor_pos in get_neighbors(grid, current.position):
            if neighbor_pos not in closed:
                new_cost = current.cost + COSTS[grid[neighbor_pos[0]][neighbor_pos[1]]]
                neighbor_node = Node(neighbor_pos, parent=current, cost=new_cost)
                f = new_cost + euclidean(neighbor_pos, end)
                heapq.heappush(open_queue, (f, neighbor_node))
    
    return None, closed, set(), 0
