grid = [
[[North],[North,East,South],[East,South],[East],[North,East],[North,South],[North,East,South],[North,South],[East,South],[East]],
[[North,East],[South,West],[East,West],[East,West],[East,West],[North,East],[South,West],[North,East],[South,West],[East,West]],
[[North,West],[East,South],[North,West],[East,South,West],[East,West],[East,West],[East],[North,West],[East,South],[East,West]],
[[North,East],[South,West],[North],[South,West],[East,West],[East,West],[North,East,West],[South],[North,West],[East,South,West]],
[[North,East,West],[East,South],[North,East],[North,South],[South,West],[East,West],[East,West],[North,East],[East,South],[East,West]],
[[East,West],[East,West],[East,West],[North,East],[East,South],[East,West],[North,West],[South,West],[East,West],[East,West]],
[[East,West],[North,West],[South,West],[East,West],[North,East,West],[South,West],[North,East],[East,South],[North,West],[East,South,West]],
[[East,West],[East],[North,East],[East,South,West],[West],[North,East],[South,West],[North,West],[East,South],[West]],
[[North,West],[East,South,West],[East,West],[West],[North,East],[South,West],[North],[East,South],[North,West],[East,South]],
[[North],[South,West],[North,West],[North,South],[North,South,West],[North,South],[South],[North,West],[North,South],[South,West]]
]
treasure = (0,9)solve_maze(grid,treasure)