"""First time creating nodes like this in python so claude was helpful
    Enumerated Char values of text file for cost
    each node carries position, parent, and cost
    list is returned in reverse order which gives Start->End
    uses index access to find neighbors relative to current node"""
COSTS = {'R': 1, 'F': 3, 'O': 5, 'H': 8, 'M': 15, 'W': None, 'S': 3, 'E': 3}
class Node:


    def __init__(self, position, parent=None, cost=0):
            self.position = position
            self.parent = parent
            self.cost = cost
    
    def __lt__(self, other):
            return self.cost < other.cost
    
def retrace_path(node):
    path = []
    while node:
        path.append(node.position)
        node = node.parent
    return list(reversed(path))

def get_neighbors(grid, position):
    directions = [(-1,0), (1,0), (0,-1),(0,1)]
    neighbors = []
    rows, cols = len(grid), len(grid[0])
    for dr, dc in directions:
        r, c = position[0] + dr, position[1] + dc
        if 0 <= r < rows and 0 <= c < cols:
            if COSTS[grid[r][c]] is not None:  # not water
                neighbors.append((r, c))
    return neighbors

