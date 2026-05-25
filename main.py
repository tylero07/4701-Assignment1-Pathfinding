from algos import *
from read_file_to_map import load_map
from display import display
import os

def run_BFS(PATHNAME):
    grid, start, end = load_map(PATHNAME)
    path, closed, open_list, cost = bfs(grid, start, end)
    print(f"\n{PATHNAME} Path length: {len(path)}")
    print(f"{PATHNAME} States explored: {len(closed)}")
    print(f"{PATHNAME} Cost: {cost}")
    display(grid, closed, open_list, path, title=PATHNAME)
    filename = os.path.basename(PATHNAME)        # "map1_stupid.txt"
    name = os.path.splitext(filename)[0]         # "map1_stupid"
    NEW_PATHNAME = f"Solutions/BFS/{name}.png"
    os.rename(PATHNAME+".png", NEW_PATHNAME)

def run_UCS(PATHNAME):
    grid, start, end = load_map(PATHNAME)
    path, closed, open_list, cost = ucs(grid, start, end)
    print(f"\n{PATHNAME} Path length: {len(path)}")
    print(f"{PATHNAME} States explored: {len(closed)}")
    print(f"{PATHNAME} Cost: {cost}")
    display(grid, closed, open_list, path, title=PATHNAME)
    filename = os.path.basename(PATHNAME)        # "map1_stupid.txt"
    name = os.path.splitext(filename)[0]         # "map1_stupid"
    NEW_PATHNAME = f"Solutions/UCS/{name}.png"
    os.rename(PATHNAME+".png", NEW_PATHNAME)

def run_GREEDY(PATHNAME):
    grid, start, end = load_map(PATHNAME)
    path, closed, open_list, cost = greedy(grid, start, end)
    print(f"\n{PATHNAME} Path length: {len(path)}")
    print(f"{PATHNAME} States explored: {len(closed)}")
    print(f"{PATHNAME} Cost: {cost}")
    display(grid, closed, open_list, path, title=PATHNAME)
    filename = os.path.basename(PATHNAME)        # "map1_stupid.txt"
    name = os.path.splitext(filename)[0]         # "map1_stupid"
    NEW_PATHNAME = f"Solutions/GREEDY_BF/{name}.png"
    os.rename(PATHNAME+".png", NEW_PATHNAME)

def run_ASTAR_MANHATTAN(PATHNAME):
    grid, start, end = load_map(PATHNAME)
    path, closed, open_list, cost = astar_manhattan(grid, start, end)
    print(f"\n{PATHNAME} Path length: {len(path)}")
    print(f"{PATHNAME} States explored: {len(closed)}")
    print(f"{PATHNAME} Cost: {cost}")
    display(grid, closed, open_list, path, title=PATHNAME)
    filename = os.path.basename(PATHNAME)
    name = os.path.splitext(filename)[0]
    NEW_PATHNAME = f"Solutions/ASTAR_MANHATTAN/{name}.png"
    os.rename(PATHNAME+".png", NEW_PATHNAME)

def run_ASTAR_EUCLIDEAN(PATHNAME):
    grid, start, end = load_map(PATHNAME)
    path, closed, open_list, cost = astar_euclidean(grid, start, end)
    print(f"\n{PATHNAME} Path length: {len(path)}")
    print(f"{PATHNAME} States explored: {len(closed)}")
    print(f"{PATHNAME} Cost: {cost}")
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

    print("\n============RUNNING UCS============")
    run_UCS("maps/map1_stupid.txt")
    run_UCS("maps/map2_simple.txt")
    run_UCS("maps/map3_complex.txt")

    print("\n============RUNNING GREEDY============")
    run_GREEDY("maps/map1_stupid.txt")
    run_GREEDY("maps/map2_simple.txt")
    run_GREEDY("maps/map3_complex.txt")

    print("\n============RUNNING A* MANHATTAN============")
    run_ASTAR_MANHATTAN("maps/map1_stupid.txt")
    run_ASTAR_MANHATTAN("maps/map2_simple.txt")
    run_ASTAR_MANHATTAN("maps/map3_complex.txt")

    print("\n============RUNNING A* EUCLIDEAN============")
    run_ASTAR_EUCLIDEAN("maps/map1_stupid.txt")
    run_ASTAR_EUCLIDEAN("maps/map2_simple.txt")
    run_ASTAR_EUCLIDEAN("maps/map3_complex.txt")