def create_list(n):
	grid = []
	for i in range(0,n,+1):
		grid.append(None)
	quick_print(i)
	return grid
	
def sunflower_measure():
	world_size = get_world_size()
	seeds = num_items(Items.Sunflower_Seed)
	grid = create_list(power(world_size,2))
	move_to(0,0)
	for i in range(len(grid)):
		plant(Entities.Sunflower)
		grid[i]= [measure(),(get_pos_x(),get_pos_y())]
		move_()
	sort_list_index(grid,0)
	
	a = world_size // 1.2
	while grid[len(grid)-1][0] > a  and seeds > world_size * 2: 
		pos = grid[len(grid)-1][1]
		move_to(pos[0], pos[1])
		while not can_harvest():
			water()
		harvest()
		plant(Entities.Sunflower)
		grid[len(grid)-1][0] = measure()
		if grid[len(grid)-1][0] < grid[len(grid)-2][0]:
			find_same_pedals(grid)
			
def clear_grid():
	while not on_board_end():
		harvest()
		move_()
	harvest()
	move_()
	def find_same_pedals(grid):
	new_pedal =  grid[len(grid)-1] 
	for i in range(len(grid)-2,-1,-1):
		pedal = grid[i][0]
		if  pedal < new_pedal[0]: 
			grid.insert(i,new_pedal)
			grid.pop(len(grid)-1)
			break
		
		