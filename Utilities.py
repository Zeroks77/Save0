def water():
	world_size = get_world_size()
	if get_water() < 0.8 and num_items(Items.Water_Tank) > 0 :
		use_item(Items.Water_Tank)
	elif num_items(Items.Wood) > get_cost(Items.Empty_Tank)[Items.Wood] * world_size:
		if num_items(Items.Water_Tank) + num_items(Items.Empty_Tank) > power(world_size,3) or num_unlocked(Unlocks.Trees) < 3:
			return
		trade(Items.Empty_Tank, world_size - 1)
		
def clear_row(rows): 
	move_to(0,0)
	world = get_world_size() * rows
	for i in range(world): 
		harvest()
		move_()
		
def fertilize():
	world_size = get_world_size()
	if can_harvest() == False  and num_items(Items.Fertilizer) > power(get_world_size(),2):
		use_item(Items.Fertilizer)
	elif num_unlocked(Unlocks.Fertilizer) > 0 and num_items(Items.Pumpkin) > get_cost(Items.Fertilizer)[Items.Pumpkin]	* world_size:
		trade(Items.Fertilizer, world_size -1)

def harvest_item(Item):
	if can_harvest():
		harvest()
		plant_item(Item)
	elif get_entity_type() == None:
		plant_item(Item)
	else: 
		water()
		
def plant_row(Item,rows):
	move_to(0,0)
	world = get_world_size() * rows
	for i in range(world):
		if can_harvest():
			harvest() 
		plant_item(Item)
		move_()		
		
def plant_field(Item):
	if Item == Items.Hay:
		return 	
	move_to(0,0)
	while not on_board_end():
		if can_harvest():
			harvest() 
		plant_item(Item)		move_()
	if can_harvest():
		harvest() 
	plant_item(Item)
	
def power(num, exp ): 
	return num ** exp	
	
def plant_item(Item):
	if Item == Items.Hay:
		return
	if Item == Items.Bones:
		use_item(Items.Egg)
		return
	if Item == Items.Wood:
		if num_unlocked(Unlocks.Trees) == 0: 
			plant(Entities.Bush)
		else:
			woodgrid()
	if get_entity_type() == None:
		plant(item_to_entity[Item]) 	
	water()
		
def farmgrid(item) : 	for i in range(get_world_size()):
		for j in range(get_world_size()):
			harvest_item(item)
			move(North)
		move(East)
				
def till_field(): 	move_to(0,0)
	while not on_board_end():
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
	while not on_board_end():
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
	if num_unlocked(Unlocks.Expand) == 1:
		return get_pos_y() == world_size
	return get_pos_x() == world_size and get_pos_y() == world_size 


	
def fill_with_board():
	world_size = get_world_size()
	position_list = []
	for i in range(world_size):
		for j in range(world_size):
			position_list.append([i,j])	return position_list
	

def trade_item(item, count):
	if item == Items.Hay or item == Items.Wood or item == Items.Gold:
		return
	needed_item = item_to_trade[item]
	cost_ = get_cost(needed_item) 
	if item == Items.Power or item ==Items.Cactus or item ==Items.Pumpkin:
		count = power(get_world_size(),2) * 2
	if item == Items.Bones:
		count = power(get_world_size(),2) * 3
	current_seeds = num_items(needed_item) 
	if current_seeds > 0:
		count -= current_seeds
	if num_items(needed_item) >= count:
		return
	for item_ in cost_:
		current_num = num_items(item_ )
		# How many of Item is needed to farm next upgrade, minus the one that allready in inventory.
		amount_of_this_item_needed = (cost_[item_ ] * count) - current_num 
		if amount_of_this_item_needed <= 0 :
			continue
		seeds_needed = ((amount_of_this_item_needed - num_items(item_)) // return_current_yield_per_tile(item_)) + 1 + get_world_size()
		trade_item(item_,amount_of_this_item_needed)
		prep(item_)
		farm_item(item_ , amount_of_this_item_needed + current_num )
	trade(needed_item ,count)

			