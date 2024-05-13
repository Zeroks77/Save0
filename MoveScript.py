def move_(): 
	y = get_pos_y()
	world = get_world_size() -1
	if y < world :
		move(North)	else:
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
	while get_entity_type() != Entities.Treasure:		pos_x = get_pos_x()
		pos_y = get_pos_y()
		move(directions[dir_check(cur_dir+1)])					
		if pos_x != get_pos_x() or pos_y != get_pos_y():
			cur_dir = dir_check(cur_dir+1)
			continue
		cur_dir = dir_check(cur_dir)		move(directions[cur_dir])
		if pos_x == get_pos_x() and pos_y == get_pos_y():			if on_same_tile == 0: 		
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
					continue				on_same_tile += 1
		else: 
			on_same_tile = 0
	a = 0
	while treasure_run > 0:
		a+=1
		a_star(treasure_run)
	harvest()
	
def a_star(loc): 
	current_run = 0
	loc = (0,0)	up_maze(loc)
	if loc == None:
		return
	x_dif = 0
	y_dif = 0
	open_list = []
	closed_list = []
	path_list = []
	drone_x = get_pos_x()
	drone_y = get_pos_y()
	open_list.append([0,[get_pos_x(),get_pos_y()]])
	while loc != (drone_x, drone_y):
		drone_x = get_pos_x()
		drone_y = get_pos_y()
		#calc weights of neighbours
		calc_weights(open_list, closed_list, loc)
		sort_dim(open_list, 0)
		loc_ = open_list[0]
		quick_print(loc_)
		move_to(loc_[1][0],loc_[1][1])
		while drone_x != get_pos_x() or drone_y != get_pos_y():
			path_list.append(loc_)
			drone_x = get_pos_x()
			drone_y = get_pos_y()
			calc_weights(open_list, closed_list, loc)			sort_dim(open_list, 0)	
			quick_print(loc_)
			move_to(loc_[1][0],loc_[1][1])
			if (drone_x,drone_y) == loc:
				return
		if len(path_list) > 0:
			last_loc = path_list.pop()
			quick_print(last_loc)
			move_to(last_loc[1][0],last_loc[1][1])

def calc_weights(open_list, closed_list, target):
	x_ = open_list[0][1][0]
	y_ = open_list[0][1][1]
	closed_list.append(open_list.pop(0))
	if in_world(x_-1):
		loc = [cost(x_-1,y_,target),[x_-1,y_]]
		if not in_closed(loc, closed_list):
			open_list.append(loc)
	if in_world(x_+1):
		loc = [cost(x_+1,y_,target),[x_+1,y_]]
		if not in_closed(loc, closed_list):
			open_list.append(loc)	if in_world(y_-1):
		loc = [cost(x_,y_-1,target),[x_,y_-1]]
		if not in_closed(loc, closed_list):
			open_list.append(loc)
	if in_world(y_+1):
		loc = [cost(x_,y_+1,target),[x_,y_+1]]
		if not in_closed(loc, closed_list):
			open_list.append(loc)

def in_world(x):
	if x < 0 or x > get_world_size():
		return False	
	return True		
		
def in_closed(loc, closed):	for i in closed: 
		if loc == i:
			return True
	return False
	def cost(x,y, target):
	return abs((target[0]-x))+ abs((target[1]-y))
	

	
def move_dir(i):	dir = {-1:East, 0:West, 1:North, 2:South }
	move(dir[i])
	
def move_dir_op(i)	:
	dir = {-1:West, 0:East, 1:South, 2:North }
	move(dir[i])
	
def CreateGrid():
	n = get_world_size()
    grid = [] 
    for x in range(n):
        row = []  
        for y in range(n):
            row.append(None)  
        grid.append(row)  
    return grid  

def up_maze(loc):
	minFertilizer = power(get_world_size(), 2) * 3
	while get_entity_type() == Entities.Treasure:
		if num_items(Items.Fertilizer) > minFertilizer: 
			use_item(Items.Fertilizer)
			loc = measure()
			if get_entity_type() != Entities.Treasure:
			continue				
		else: 
			harvest()
			loc = None
def dir_check(dir) : 	if dir > 3:
		dir -= 4
	if dir < 0:
		dir += 4	return dir
				
		
		