grid = [
[[East],[North,East],[North,South],[North,South],[North,East,South],[North,South],[East,South],[North],[North,South],[East,South]],
[[East,West],[East,West],[East],[North,East],[South,West],[North],[North,South,West],[North,South],[North,South],[East,South,West]],
[[East,West],[North,West],[East,South,West],[North,West],[North,South],[East,South],[North,East],[East,South],[North],[East,South,West]],
[[East,West],[North,East],[South,West],[North,East],[South],[North,West],[East,South,West],[North,West],[East,South],[West]],
[[East,West],[East,West],[North,East],[South,West],[North,East],[South],[North,West],[East,South],[North,West],[East,South]],
[[East,West],[East,West],[East,West],[North,East],[South,West],[North,East],[East,South],[East,West],[East],[East,West]],
[[East,West],[North,West],[East,South,West],[North,West],[East,South],[East,West],[West],[North,East,West],[South,West],[East,West]],
[[North,East,West],[North,South],[South,West],[East],[East,West],[North,East,West],[North,South],[South,West],[North,East],[East,South,West]],
[[North,West],[North,South],[North,South],[East,South,West],[East,West],[West],[North,East],[East,South],[East,West],[East,West]],
[[North],[North,South],[North,South],[South,West],[North,West],[North,South],[South,West],[North,West],[South,West],[West]]
]
treasure = (3,9)
print_grid(grid)solve_maze(grid,treasure)