from display import display
from read_file_to_map import load_map
grid, start, end = load_map("maps/map1_stupid.txt")

display(grid, closed=set(), open_list=set(), path=[], title="test")
# debugging print
print(start, end)

grid, start, end = load_map("maps/map2_simple.txt")

display(grid, closed=set(), open_list=set(), path=[], title="test")
# debugging print
print(start, end)

grid, start, end = load_map("maps/map3_complex.txt")

display(grid, closed=set(), open_list=set(), path=[], title="test")
# debugging print
print(start, end)