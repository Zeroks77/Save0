def cactus_measure(): 
	grid = grid_dimentional()
	for i in range(len(grid)):
		for j in range(len(grid)):
			move_to(i,j)
			grid[i][j] = measure()
	a = 0
	while not grid_sorted(grid):
		for i in range(len(grid)):
			for j in range(len(grid)):
				if in_world(i+1) and grid[i][j] > grid[i+1][j]:
					move_to(i,j)
					swap(East)
					grid[i][j], grid[i+1][j] = grid[i+1][j], grid[i][j]
				if in_world(j+1) and grid[i][j] > grid[i][j+1]:
					move_to(i,j)					swap(North)
					grid[i][j], grid[i][j+1] = grid[i][j+1], grid[i][j]
	move_to(0,0)
	harvest()
		
def grid_sorted(grid):
	for i in range(len(grid)):
		for j in range(len(grid)):
			if not in_world(i+1) or in_world(j+1): 
				continue
			if  grid[i][j] > grid[i+1][j] or grid[i][j] > grid[i][j]+1:
				return False	return True

def grid_dimentional():
	grid = []
	world_size = get_world_size()
	for j in range(world_size):
		row = []
		for i in range(world_size):
			row.append([])
		grid.append(row)
	return grid