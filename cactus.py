def cactus_measure(): 
	world_size = get_world_size()
	
	def grid_sorted(grid):
		for i in range(len(grid)):
			for j in range(len(grid)):
				if not in_world(i+1,j+1): 
					continue
				if  grid[i][j] > grid[i+1][j] or grid[i][j] > grid[i][j]+1:
					return False		
		return True
	def in_world(x,y):
		x_in_world = 0 <= x and x <= world_size -1
		y_in_world = 0 <= y and y <= world_size -1
		return  (x_in_world and y_in_world)
 
	def grid_dimentional():
		grid = []
		for j in range(world_size):
			row = []
			for i in range(world_size):
				row.append([])
			grid.append(row)
		return grid
		
	
	grid = grid_dimentional()	
	for i in range(len(grid)):
		for j in range(len(grid)):
			move_to(i,j) 
			grid[i][j] = measure()
			if grid[i][j] == None:				return
	a = 0
	while not grid_sorted(grid):
		for i in range(len(grid)):
			for j in range(len(grid)):
				if in_world(i+1,j) and grid[i][j] > grid[i+1][j]:
					move_to(i,j)
					swap(East)
					grid[i][j], grid[i+1][j] = grid[i+1][j], grid[i][j]
				if in_world(i,j+1) and grid[i][j] > grid[i][j+1]:
					move_to(i,j)					swap(North)
					grid[i][j], grid[i][j+1] = grid[i][j+1], grid[i][j]
	move_to(0,0)
	harvest()
		
