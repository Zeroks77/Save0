def move_(): 
	y = get_pos_y()
	world = get_world_size() -1
	if y < world :
		move(North)
	else:
		move(East)
		move(North)
		
def debug(dir): 
	quick_print(get_pos_x(), get_pos_y())
	move(dir)
	
def move_to(x,y):
    def half_mod(x, n):
        return (x + n // 2) % n - n // 2

    n = get_world_size()
    x = half_mod(x - get_pos_x(), n)
    y = half_mod(y - get_pos_y(), n)

    for i in range(abs(x)):
        if x > 0:
            move(East)
        else:
            move(West)

    for i in range(abs(y)):
        if y > 0:
            move(North)
        else:
            move(South)

def navigate_maze():
	cur_dir = 0
	directions = [South,West,North, East]
	oposite_direction= [North, East, South,West]
	pos_x = 0
	pos_y = 0
	on_same_tile = 0
	treasure_run = 10
	while get_entity_type() != Entities.Treasure:		
		pos_x = get_pos_x()
		pos_y = get_pos_y()
		move(directions[dir_check(cur_dir+1)])					
		if pos_x != get_pos_x() or pos_y != get_pos_y():
			cur_dir = dir_check(cur_dir+1)
			continue
		cur_dir = dir_check(cur_dir)		
		move(directions[cur_dir])
		if pos_x == get_pos_x() and pos_y == get_pos_y():			
			if on_same_tile == 0: 		
				move(directions[dir_check(cur_dir+1)])					
				if pos_x != get_pos_x() or pos_y != get_pos_y():
					on_same_tile = 0
					cur_dir +=1
					continue
			if on_same_tile == 1: 		
				move(directions[dir_check(cur_dir-1)])					
				if pos_x != get_pos_x() or pos_y != get_pos_y():
					on_same_tile = 0
					cur_dir -=1
					continue
			elif on_same_tile == 2:
				move(oposite_direction[cur_dir])
				if pos_x != get_pos_x() or pos_y != get_pos_y():
					on_same_tile = 0
					cur_dir +=2
					continue				
			on_same_tile += 1
		else: 
			on_same_tile = 0
	current_run = 0
	while treasure_run > current_run:
		current_run+=1
		a_star(current_run)
		if current_run == -1: 
			return
	harvest()
	
def a_star(current_run): 
	loc = up_maze(current_run)
	if loc == None:
		return
	x_dif = 0
	y_dif = 0
	open_list = []
	closed_list = []
	path_list = []
	drone_x = get_pos_x()
	drone_y = get_pos_y()
	open_list.append([cost(drone_x,drone_y,loc),[drone_x,drone_y]])
	while loc != (drone_x, drone_y):
		drone_x = get_pos_x()
		drone_y = get_pos_y()
		#calc weights of neighbours
		calc_weights(open_list, closed_list, loc)
		sort_dim(open_list, 0)
		loc_ = open_list[0]
		quick_print(loc_ , (drone_x, drone_y))
		move_maze((loc_[1]))
		while drone_x != get_pos_x() or drone_y != get_pos_y():
			path_list.append(loc_)
			drone_x = get_pos_x()
			drone_y = get_pos_y()
			calc_weights(open_list, closed_list, loc)			
			sort_dim(open_list, 0)	
			loc_ = open_list[0]
			quick_print(loc_ , (drone_x, drone_y))
			move_maze((loc_[1]))
			if (drone_x,drone_y) == loc:
				return
		while (drone_x,drone_y) == (get_pos_x(), get_pos_y()):
			#go back
			open_list.insert(0,closed_list[len(closed_list)-1])
			calc_weights(open_list, closed_list, loc)
			sort_dim(open_list, 0)
			loc_ = open_list[0]
			quick_print(loc_ , (drone_x, drone_y))
			move_maze((loc_[1]))
		if len(path_list) > 0:
			last_loc = path_list.pop()
			quick_print(loc_ , (drone_x, drone_y), "Move back")
			open_list.append(last_loc)
			move_maze((loc_[1]))

def calc_weights(open_list, closed_list, target):
	x_ = open_list[0][1][0]
	y_ = open_list[0][1][1]
	closed_list.append(open_list.pop(0))
	if in_world(x_-1):
		loc = [cost(x_-1,y_,target),[x_-1,y_]]
		if not in_list(loc, closed_list) and not in_list(loc, open_list):
			open_list.append(loc)
	if in_world(x_+1):
		loc = [cost(x_+1,y_,target),[x_+1,y_]]
		if not in_list(loc, closed_list) and not in_list(loc, open_list):
			open_list.append(loc)	
	if in_world(y_-1):
		loc = [cost(x_,y_-1,target),[x_,y_-1]]
		if not in_list(loc, closed_list) and not in_list(loc, open_list):
			open_list.append(loc)
	if in_world(y_+1):
		loc = [cost(x_,y_+1,target),[x_,y_+1]]
		if not in_list(loc, closed_list) and not in_list(loc, open_list):
			open_list.append(loc)

def in_world(x):
	if x < 0 or x > get_world_size()-1:
		return False	
	return True		
		
def in_list(loc, list):	
	for i in list: 
		if loc == i:
			return True
	return False
def cost(x,y, target):
	return abs((target[0]-x))+ abs((target[1]-y))
	
def move_maze(target):
	cur_x = get_pos_x()
	cur_y = get_pos_y()
	dir_x = target[0] - cur_x	dir_y = target[1] - cur_y
	if dir_x != 0:
		move_x(dir_x)
	if dir_y != 0:
		move_y(dir_y)
def move_x(x):
	dir = {-1:West, 1: East}
	move(dir[x])
def move_y(y):
	dir = {-1:South, 1: North}
	move(dir[y])
def CreateGrid():
	n = get_world_size()
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
			
def dir_check(dir) : 	
	if dir > 3:
		dir -= 4
	if dir < 0:
		dir += 4	
	return dir
				
		
		