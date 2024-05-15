def water():
	if can_harvest() == False and get_water() < 1 and num_items(Items.Water_Tank) > 15:
		use_item(Items.Water_Tank)
def fertilize():
	if can_harvest() == False  and num_items(Items.Fertilizer) > power(get_world_size(),3):
		use_item(Items.Fertilizer)
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
	move_to(0,0)
	
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
	if Item == Items.Bones: 
		if get_entity_type() != None and get_entity_type() != Entities.Dinosaur:
			harvest()
		if get_entity_type() == Entities.Grass and num_items(Items.Egg) > power(get_world_size(),2):
			use_item(Items.Egg)
			
	if Item == Items.Cactus:
		if get_entity_type() != None and get_entity_type() != Entities.Cactus:
			harvest()
		if get_entity_type() == None and num_items(Items.Cactus_Seed) > power(get_world_size(),2):
			plant(Entities.Cactus)
	water()
		
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


	
def fill_with_board():
	world_size = get_world_size()
	position_list = []
	for i in range(world_size):
		for j in range(world_size):
			position_list.append([i,j])	return position_list
	
	

			