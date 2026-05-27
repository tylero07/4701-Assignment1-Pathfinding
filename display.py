"""Display file for all of the visualization instead of ascii per instructions
    ***Code generatied by claude Sonnet 4.6***
    inline comments added for my own understanding"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.ticker import MultipleLocator

ax = plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(5))   # labels every 5
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.xaxis.set_minor_locator(MultipleLocator(1))   # lines every 1
ax.yaxis.set_minor_locator(MultipleLocator(1))
ax.grid(True, which='minor', color='black', linewidth=0.3, alpha=0.5)
ax.grid(True, which='major', color='black', linewidth=0.3, alpha=0.5)

# terrain color definitions
TERRAIN_COLORS = {
    'R': [1.0, 0.9, 0.0],    # yellow - road
    'F': [0.5, 0.8, 0.3],    # green - field
    'O': [0.2, 0.5, 0.1],    # dark green - forest
    'H': [0.6, 0.4, 0.2],    # brown - hills
    'M': [0.5, 0.5, 0.5],    # grey - mountains
    'W': [0.1, 0.3, 0.9],    # blue - water
    'S': [1.0, 1.0, 1.0],    # white - start
    'E': [0.0, 0.0, 0.0],    # black - end
}

def display(grid, closed, open_list, path, title=""):
    rows = len(grid)
    cols = len(grid[0])
    
    # build base terrain image
    img = np.zeros((rows, cols, 3))
    for r in range(rows):
        for c in range(cols):
            img[r][c] = TERRAIN_COLORS[grid[r][c]]
    
    plt.figure(figsize=(8, 8))
    plt.imshow(img)
    
    # overlay explored, frontier, path
    for (r, c) in closed:
        plt.plot(c, r, 's', color='red', alpha=0.3, markersize=4)
    for (r, c) in open_list:
        plt.plot(c, r, 's', color='orange', alpha=0.3, markersize=4)
    for (r, c) in path:
        plt.plot(c, r, 's', color='white', alpha=0.9, markersize=4)
    
    # visible legend on map
    legend = [
    mpatches.Patch(color=[1.0, 0.9, 0.0], label='Road (1)'),
    mpatches.Patch(color=[0.5, 0.8, 0.3], label='Field (3)'),
    mpatches.Patch(color=[0.2, 0.5, 0.1], label='Forest (5)'),
    mpatches.Patch(color=[0.6, 0.4, 0.2], label='Hills (8)'),
    mpatches.Patch(color=[0.5, 0.5, 0.5], label='Mountains (15)'),
    mpatches.Patch(color=[0.1, 0.3, 0.9], label='Water (impassable)'),
    mpatches.Patch(color='white', label='Start / Path'),
    mpatches.Patch(color='black', label='End'),
    mpatches.Patch(color='red', alpha=0.5, label='Explored'),
    mpatches.Patch(color='orange', alpha=0.5, label='Frontier'),
    ]
    plt.legend(handles=legend, loc='upper right', fontsize=7)

    plt.legend(handles=legend, loc='upper right')
    plt.title(title)
    plt.xticks(range(cols))
    plt.yticks(range(rows))
    plt.grid(True, color='black', linewidth=0.3, alpha=0.5) # adds lines around cells
    plt.savefig(f"{title}.png", dpi=150, bbox_inches='tight')
    