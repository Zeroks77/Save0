def water():
	if can_harvest() == False and get_water() < 1 and num_items(Items.Water_Tank) > 15:
		use_item(Items.Water_Tank)
def harvest_item(Item):
	if can_harvest():
		harvest()
		plant_item(Item)
	elif get_entity_type() == None:
		plant_item(Item)
	else: 
		water()
def initial_plant(Item):
	move_to(0,0)
	while on_board_end() == False: 
		plant_item(Item)		move_()
	plant_item(Item)
	
def power(num, exp ): 
	res = num 
	for i in range(exp -1):
		res *= num	
	return res	
		
def plant_item(Item):
	water()
	if Item == Items.Hay:
		return
	if Item == Items.Carrot:
		if get_entity_type() != None:
			harvest()
		if get_entity_type() == None and num_items(Items.Carrot_Seed) > power(get_world_size(),2):
			plant(Entities.Carrots) 	
	if Item == Items.Wood:
		if get_entity_type() != None:
			harvest()
		woodgrid()
	if Item == Items.Pumpkin:
		if get_entity_type() != None:
			harvest()
		if get_entity_type() == None and num_items(Items.Pumpkin_Seed) > power(get_world_size(),2):
			plant(Entities.Pumpkin)
	if Item == Items.Power: 	
		if get_entity_type() != None and get_entity_type() != Entities.Sunflower:
			harvest()
		if get_entity_type() == None and num_items(Items.Sunflower_Seed) > power(get_world_size(),2):
			plant(Entities.Sunflower)
			
def woodgrid():	if (get_pos_x() % 2 == 0 and get_pos_y() % 2 == 1) or (get_pos_x() % 2 == 1 and get_pos_y() % 2 == 0) :
		plant(Entities.Tree)	else:		plant(Entities.Bush)
		
def farmgrid(item) : 	for i in range(get_world_size()):
		for j in range(get_world_size()):
			harvest_item(item)
			move(North)
		move(East)
				
def till_field(): 	move_to(0,0)
	while on_board_end() == False:
		if get_ground_type() == Grounds.Turf:
			if get_entity_type() != None:
				harvest()
			till()
		move_()
	if get_ground_type() == Grounds.Turf:
			if get_entity_type() != None:
				harvest()
			till()

def untill_field():
	move_to(0,0)
	while on_board_end() == False:
		if get_ground_type() == Grounds.Soil:
			if get_entity_type() != None:
				harvest()
			till()
		move_()
	if get_ground_type() == Grounds.Soil:
			if get_entity_type() != None:
				harvest()
			till()
	
def on_board_end(): 	
	world_size = get_world_size()-1
	return get_pos_x() == world_size and get_pos_y() == world_size 


def pumpkin_measure():
	move_to(0,0)
	check_positions = fill_with_board()
	while len(check_positions) != 0:
			if num_items(Items.Pumpkin_Seed) == 0:
				check_positions = []
				break
			pos = check_positions.pop()
			move_to(pos[0],pos[1])
			if get_entity_type() == None:
				check_positions.insert(0,pos)
				plant(Entities.Pumpkin)
	harvest_item(Items.Pumpkin)
	
def fill_with_board():
	world_size = get_world_size()
	position_list = []
	for i in range(world_size):
		for j in range(world_size):
			position_list.append([i,j])	return position_list
	
	
def sunflower_measure():
	most_pedals = [0,0,0] 
	initial_plant(Items.Power)
	harvested = False
	move_to(0,0)
	world_size = get_world_size()
	seeds = num_items(Items.Sunflower_Seed)
	check_positions = fill_with_board()
	while not seeds < power(get_world_size(),2) * 2: 
		if  len(check_positions) == 0:
			move_to(most_pedals[0], most_pedals[1])
			harvest_item(Items.Power)
			most_pedals = [0,0,0] 
			check_positions = fill_with_board()			
			move_to(0,0)		pos = check_positions.pop()
		move_to(pos[0],pos[1])
		if can_harvest() == False:
			check_positions.insert(0,pos)
		a = measure()
		if a != None and a > most_pedals[2]:
			most_pedals = [get_pos_x(),get_pos_y(),a]
		if a == None: 
			move_to(0,0)
			break
		
			