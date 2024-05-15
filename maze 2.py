def map_maze():
	grid = CreateGrid(get_world_size())
	dirs = [North, East, South, West]
    dir_change = { True: 3, False: 1}
    dir = 0
    treasure = ()
	while not visited_every_cell(grid):
		x_ = get_pos_x()
		y_ = get_pos_y()
		if get_entity_type() == Entities.Treasure:
			treasure = (x_,y_)
		if grid[x_][y_] == None:
			grid[x_][y_] =  direction_check()
		dir = (dir + dir_change[move(dirs[dir])]) % 4
	for x in range(10):		quick_print(grid[x])#solve_maze(grid, treasure)
	
def solve_maze(grid, treasure):
	x_, y_ = get_pos_x(), get_pos_y()
	path = []
	path.insert(0,[treasure, None] )
	x_dir = {West: -1, East: 1,South: 0, North: 0}
	y_dir = {South: -1, North: 1,West: 0, East: 0}
	dir_ops = {North : South, West: East, South: North, East:West}
	dirs = grid[treasure[0]][treasure[1]]
	x,y = treasure[0],treasure[1]
	next_step = [100,(treasure[0],treasure[1]), None]
	while True:
		if path[0][0] == (x_,y_):
			path.pop(0)
			for p in path: 
				maze_move_to(p[0][0],p[0][1])
			break
		if len(dirs) == 1:
			x,y = path[0][0][0] + x_dir[dirs[0]], path[0][0][1] + y_dir[dirs[0]] 
			if not in_list(path, [(x,y),dir_ops[dirs[0]]]):
				path.insert(0,[(x,y), dirs[0]])
			dirs = grid[x][y]
		else:
			next_step = [100,(treasure[0],treasure[1]), None]
			for d in dirs: 
				x,y = path[0][0][0]+ x_dir[d], path[0][0][1] + y_dir[d] 
				if in_list(path,[(x,y),dir_ops[d]]):
					continue
				a = cost(x,y,(x_,y_))
				if next_step[0] > a and not in_list(path, [(x,y),d]) and (x,y) != treasure: 
					next_step = [a,(x,y),d]
			
			if next_step[2] == None or ([(next_step[1][0],next_step[1][1]),next_step[2]] == path[0] or in_list(path, [(next_step[1][0],next_step[1][1]),dir_ops[next_step[2]]])):
				t= path.pop(0)
				d = t[1]
				x,y = t[0][0] + x_dir[d]* -1, t[0][1] + y_dir[d] * -1
				dirs = grid[x][y]
				dirs.remove(d)
				continue
			if not in_list(path, [(next_step[1][0],next_step[1][1]),next_step[2]]):
				path.insert(0,[next_step[1], next_step[2]])
				dirs = grid[next_step[1][0]][next_step[1][1]] 
			
		
def maze_move_to(x,y) : 
	x_ = get_pos_x()
	y_ = get_pos_y()
	if x != x_:
		if x - x_ == 1: 
			move(East)
		else:
			move(West)
	if 	y != y_: 
		if y - y_ == 1: 
			move(North)
		else:
			move(South)			
def cost(x,y, target):
	return abs((target[0]-x))+ abs((target[1]-y))
	
def in_list(list, coord):
	for i in list: 
		if 	coord == i :
			return True
	return False
	
def visited_every_cell(grid): 
	for i in grid:
		for j in i:
			if j == None:
				return False
	return True
	
def direction_check():
    x_ = get_pos_x()
    y_ = get_pos_y()
    dirs = [North, East, South, West]
    dirs_ = {North:South, East:West, South:North, West:East} 
	a = []
	for i in dirs:
		moved = move(i)
		if moved:
			move(dirs_[i])
			a.append(i)
	return a 

def in_world(x):
	if x < 0 or x > get_world_size()-1:
		return False	
	return True		



def CreateGrid(n):
    grid = [] 
    for x in range(n):
        row = []  
        for y in range(n):
            row.append(None)  
        grid.append(row)  
    return grid  

def up_maze(current_run):
	minFertilizer = power(get_world_size(), 2) * 3
	loc = measure()
	while get_entity_type() == Entities.Treasure:
		if num_items(Items.Fertilizer) > minFertilizer: 
			use_item(Items.Fertilizer)
			if get_entity_type() != Entities.Treasure:
				continue				
		else: 
			harvest()
			current_run= -1
			loc = None
	return loc
				
