from algos import bfs
from read_file_to_map import load_map
from display import display
import os

def run_BFS(PATHNAME):
    grid, start, end = load_map(PATHNAME)
    path, closed, open_list = bfs(grid, start, end)
    print(f"Path length: {len(path)}")
    print(f"States explored: {len(closed)}")
    display(grid, closed, open_list, path, title=PATHNAME)
    filename = os.path.basename(PATHNAME)        # "map1_stupid.txt"
    name = os.path.splitext(filename)[0]         # "map1_stupid"
    NEW_PATHNAME = f"Solutions/BFS/{name}.png"
    os.rename(PATHNAME+".png", NEW_PATHNAME)


if __name__ == "__main__":
    run_BFS("maps/map1_stupid.txt")
    run_BFS("maps/map2_simple.txt")
    run_BFS("maps/map3_complex.txt")

