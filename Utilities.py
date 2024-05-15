def water():
	world_size = get_world_size()
	if can_harvest() == False and get_water() < 1 and num_items(Items.Water_Tank) > power(world_size,2):
		use_item(Items.Water_Tank)
	elif num_items(Items.Water_Tank) == 0 or (num_items(Items.Water_Tank) + num_items(Items.Empty_Tank) < power(world_size,2) * 2  and num_items(Items.Wood) > get_cost(Items.Empty_Tank)[Items.Wood]	* world_size):
		trade(Items.Empty_Tank, world_size - 1)
def fertilize():
	world_size = get_world_size()
	if can_harvest() == False  and num_items(Items.Fertilizer) > power(get_world_size(),3):
		use_item(Items.Fertilizer)
	elif num_unlocked(Unlocks.Fertilizer) > 0 and num_items(Items.Pumpkin) > get_cost(Items.Fertilizer)[Items.Pumpkin]	* world_size:
		trade(Items.Fertilizer, world_size - 1)
def harvest_item(Item):
	if can_harvest():
		harvest()
		plant_item(Item)
	elif get_entity_type() == None:
		plant_item(Item)
	else: 
		water()
def initial_plant(Item):
	if Item == Items.Hay:
		return
	if not Item == Items.Cactus and not Item == Items.Power and not Item == Items.Bones:
		harvest()  
	move_to(0,1)
	while on_board_end() == False: 
		plant_item(Item)		move_()
	plant_item(Item)
	
def power(num, exp ): 
	res = num 
	for i in range(exp -1):
		res *= num	
	return res		
	
def plant_item(Item):
	if Item == Items.Hay:
		return
	if Item == Items.Carrot:
		if get_entity_type() == None and num_items(Items.Carrot_Seed) > power(get_world_size(),2):
			plant(Entities.Carrots) 	
	if Item == Items.Wood:
		if num_unlocked(Unlocks.Trees) == 0: 
			plant(Entities.Bush)
		else:
			woodgrid()
	if Item == Items.Pumpkin:
		if get_entity_type() == None and num_items(Items.Pumpkin_Seed) > power(get_world_size(),2):
			plant(Entities.Pumpkin)
	if Item == Items.Power: 	
		if get_entity_type() == None and num_items(Items.Sunflower_Seed) > power(get_world_size(),2):
			plant(Entities.Sunflower)
	if Item == Items.Bones: 
		if get_entity_type() == Entities.Grass and num_items(Items.Egg) > power(get_world_size(),2):
			use_item(Items.Egg)
	if Item == Items.Cactus:
		if get_entity_type() == None and num_items(Items.Cactus_Seed) > power(get_world_size(),2):
			plant(Entities.Cactus)
		
def farmgrid(item) : 	for i in range(get_world_size()):
		for j in range(get_world_size()):
			harvest_item(item)
			move(North)
		move(East)
				
def till_field(): 	move_to(0,1)
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
	move_to(0,1)
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
	return get_pos_x() == 0 and get_pos_y() == 0 


	
def fill_with_board():
	world_size = get_world_size()
	position_list = []
	for i in range(world_size):
		for j in range(world_size):
			position_list.append([i,j])	return position_list
	

def trade_item(item):
	trade_item = {
	Items.Cactus : Items.Cactus_Seed, 
	Items.Carrot : Items.Carrot_Seed, 
	Items.Pumpkin: Items.Pumpkin_Seed, 
	Items.Bones: Items.Egg, 
	Items.Power: Items.Sunflower_Seed
	}
	cost_ = get_cost(trade_item[item])
	world_size = get_world_size()
	for item_ in cost_:
		amount_of_this_item_needed = cost_[item_ ] * power(world_size,2) 
		if amount_of_this_item_needed <= num_items(item_ ):
			trade(trade_item[item],amount_of_this_item_needed)
			return
		prep(item)
		while amount_of_this_item_needed > num_items(item_ ):
			farm_item(item_ , amount_of_this_item_needed)
		
	trade(trade_item[item],amount_of_this_item_needed)

			