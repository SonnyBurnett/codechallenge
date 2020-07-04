# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?
def solve(grid_max):
    # using pascals triangle
    grid = list()
    for y in range(0,grid_max+1):
        grid.append(list())
        for x in range(0,grid_max+1):
            if y == 0:
                grid[y].append(1)
            elif x == 0:
                grid[y].append(1)
            elif x > 0:
                grid[y].append(grid[y-1][x]+grid[y][x-1])
    print(grid)

if __name__ == "__main__":
    solve(2)
    solve(3)
    solve(4)
    solve(20)
    pass