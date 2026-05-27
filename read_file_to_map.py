"""Function definition for loading maps from filepath and creating
    2D tuple and getting start and end points
    basic reads the file in in by line into grid and storing start and end
"""
def load_map(map_filepath)->tuple[list, tuple, tuple]:
    map_grid = []
    start, end = None, None
    with open(map_filepath) as file:
        for r, line in enumerate(file):
            row = list(line.strip())
            for c, char in enumerate(row):
                if char == 'S':
                    start = (r,c)
                elif char == 'E':
                    end = (r, c)
            map_grid.append(row)
    # debugging print
    # print(map_grid)
    return map_grid, start, end
