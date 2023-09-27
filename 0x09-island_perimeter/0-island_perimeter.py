#!/usr/bin/python3
""" Island perimeter"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented
    by a binary grid.

    Args:
        grid (List[List[int]]): A 2D grid where
        1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # Count top edge
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Count bottom edge
                if i == len(grid) - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Count left edge
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Count right edge
                if j == len(grid[0]) - 1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter

