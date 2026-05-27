"""Main file program can be ran from. Paths are relative
"""
import os
from algos import *
from display import display
from read_file_to_map import load_map

"""Run BFS returning needed info for tables and writeup 
"""
def run_BFS(PATHNAME):
    grid, start, end = load_map(PATHNAME)
    path, closed, open_list, cost = bfs(grid, start, end)
    print(f"\n{PATHNAME} Path Length: {len(path)}")
    print(f"{PATHNAME} Cost: {cost}")
    print(f"{PATHNAME} States Explored (Closed List): {len(closed)}")
    print(f"{PATHNAME} States Remaining (Open List): {len(open_list)}")
    display(grid, closed, open_list, path, title=PATHNAME)
    filename = os.path.basename(PATHNAME)        # mod the base pathname to place solutions
    name = os.path.splitext(filename)[0]         # for file sorting
    NEW_PATHNAME = f"Solutions/BFS/{name}.png"
    os.rename(PATHNAME+".png", NEW_PATHNAME)

"""run UCS for tables and writeup
"""
def run_UCS(PATHNAME):
    grid, start, end = load_map(PATHNAME)
    path, closed, open_list, cost = ucs(grid, start, end)
    print(f"\n{PATHNAME} Path Length: {len(path)}")
    print(f"{PATHNAME} Cost: {cost}")
    print(f"{PATHNAME} States Explored (Closed List): {len(closed)}")
    print(f"{PATHNAME} States Remaining (Open List): {len(open_list)}")
    display(grid, closed, open_list, path, title=PATHNAME)
    filename = os.path.basename(PATHNAME)        
    name = os.path.splitext(filename)[0]         
    NEW_PATHNAME = f"Solutions/UCS/{name}.png"
    os.rename(PATHNAME+".png", NEW_PATHNAME)

"""Greedy algo
"""
def run_GREEDY(PATHNAME):
    grid, start, end = load_map(PATHNAME)
    path, closed, open_list, cost = greedy(grid, start, end)
    print(f"\n{PATHNAME} Path Length: {len(path)}")
    print(f"{PATHNAME} Cost: {cost}")
    print(f"{PATHNAME} States Explored (Closed List): {len(closed)}")
    print(f"{PATHNAME} States Remaining (Open List): {len(open_list)}")
    display(grid, closed, open_list, path, title=PATHNAME)
    filename = os.path.basename(PATHNAME)        
    name = os.path.splitext(filename)[0]         
    NEW_PATHNAME = f"Solutions/GREEDY_BF/{name}.png"
    os.rename(PATHNAME+".png", NEW_PATHNAME)

"""AStar with manhattan heuristic
"""
def run_ASTAR_MANHATTAN(PATHNAME):
    grid, start, end = load_map(PATHNAME)
    path, closed, open_list, cost = astar_manhattan(grid, start, end)
    print(f"\n{PATHNAME} Path Length: {len(path)}")
    print(f"{PATHNAME} Cost: {cost}")
    print(f"{PATHNAME} States Explored (Closed List): {len(closed)}")
    print(f"{PATHNAME} States Remaining (Open List): {len(open_list)}")
    display(grid, closed, open_list, path, title=PATHNAME)
    filename = os.path.basename(PATHNAME)
    name = os.path.splitext(filename)[0]
    NEW_PATHNAME = f"Solutions/ASTAR_MANHATTAN/{name}.png"
    os.rename(PATHNAME+".png", NEW_PATHNAME)

"""Euclidian AStar
"""
def run_ASTAR_EUCLIDEAN(PATHNAME):
    grid, start, end = load_map(PATHNAME)
    path, closed, open_list, cost = astar_euclidean(grid, start, end)
    print(f"\n{PATHNAME} Path Length: {len(path)}")
    print(f"{PATHNAME} Cost: {cost}")
    print(f"{PATHNAME} States Explored (Closed List): {len(closed)}")
    print(f"{PATHNAME} States Remaining (Open List): {len(open_list)}")
    display(grid, closed, open_list, path, title=PATHNAME)
    filename = os.path.basename(PATHNAME)
    name = os.path.splitext(filename)[0]
    NEW_PATHNAME = f"Solutions/ASTAR_EUCLIDEAN/{name}.png"
    os.rename(PATHNAME+".png", NEW_PATHNAME)   

if __name__ == "__main__":
    print("============RUNNING BFS============")
    run_BFS("maps/map1_stupid.txt")
    run_BFS("maps/map2_simple.txt")
    run_BFS("maps/map3_complex.txt")
    run_BFS("maps/map4_gauntlet.txt")

    print("\n============RUNNING UCS============")
    run_UCS("maps/map1_stupid.txt")
    run_UCS("maps/map2_simple.txt")
    run_UCS("maps/map3_complex.txt")
    run_UCS("maps/map4_gauntlet.txt")

    print("\n============RUNNING GREEDY============")
    run_GREEDY("maps/map1_stupid.txt")
    run_GREEDY("maps/map2_simple.txt")
    run_GREEDY("maps/map3_complex.txt")
    run_GREEDY("maps/map4_gauntlet.txt")

    print("\n============RUNNING A* MANHATTAN============")
    run_ASTAR_MANHATTAN("maps/map1_stupid.txt")
    run_ASTAR_MANHATTAN("maps/map2_simple.txt")
    run_ASTAR_MANHATTAN("maps/map3_complex.txt")
    run_ASTAR_MANHATTAN("maps/map4_gauntlet.txt")

    print("\n============RUNNING A* EUCLIDEAN============")
    run_ASTAR_EUCLIDEAN("maps/map1_stupid.txt")
    run_ASTAR_EUCLIDEAN("maps/map2_simple.txt")
    run_ASTAR_EUCLIDEAN("maps/map3_complex.txt")
    run_ASTAR_EUCLIDEAN("maps/map4_gauntlet.txt")