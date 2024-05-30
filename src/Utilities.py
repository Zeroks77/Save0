def water():
	world_size = get_world_size()
	if get_water() < 0.8 and num_items(Items.Water_Tank) > 0 :
		use_item(Items.Water_Tank)
	elif num_items(Items.Wood) > get_cost(Items.Empty_Tank)[Items.Wood] * world_size:
		if num_items(Items.Water_Tank) + num_items(Items.Empty_Tank) > world_size**3:
			return
		trade(Items.Empty_Tank,world_size)
		use_item(Items.Water_Tank)
		
def clear_row(rows, half = False):
	move_to(0,0)
	world = get_world_size() * rows 
	if half:
		world = world // 2
	for i in range(world): 
		harvest()
		move_()
		
def fertilize():
	world_size = get_world_size()
	if can_harvest() == False  and num_items(Items.Fertilizer) > 0:
		use_item(Items.Fertilizer)
	elif num_unlocked(Unlocks.Fertilizer) > 0 and num_items(Items.Pumpkin) > get_cost(Items.Fertilizer)[Items.Pumpkin]	* world_size:
		trade(Items.Fertilizer, world_size -1)
		use_item(Items.Fertilizer)

def harvest_item(Item):
	if can_harvest():
		harvest()
		plant_item(Item)
	elif get_entity_type() == None:
		plant_item(Item)
	else: 
		water()
		
def plant_row(Item,rows = get_world_size(), half = False):
	move_to(0,0)
	world = get_world_size() * rows
	if half:
		world = world // 2
	for i in range(world):
		if can_harvest():
			harvest() 
		till_()
		plant_item(Item)
		move_()
	if can_harvest():
		harvest() 	plant_item(Item)		
		
def plant_field(Item):
	move_to(0,0)
	while not on_board_end():
		if  get_entity_type() != item_to_entity[Item]:
			harvest() 
		plant_item(Item)		move_()
	if get_entity_type() != item_to_entity[Item]:
		harvest()
	plant_item(Item)
	
def power(num, exp ): 
	return num ** exp	
	
def plant_item(Item):
	if Item == Items.Bones:
		use_item(Items.Egg)
		return
	if Item == Items.Wood:
		if num_unlocked(Unlocks.Trees) == 0: 
			plant(Entities.Bush)
		else:
			woodgrid()
	if get_entity_type() == None:
		till_()
		plant(item_to_entity[Item]) 	
	water()
		
def farmgrid(item) : 	while not on_board_end():
		harvest_item(item)
		move_()
	harvest_item(item)
	move_()
				
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
def till_():
	if get_ground_type() == Grounds.Turf:
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
	world_size = range(get_world_size())
	position_list = []
	for i in world_size:
		for j in world_size:
			position_list.append([i,j])	return position_list
	

def trade_item(item, count):
	if item == Items.Hay or item == Items.Wood or item == Items.Gold:
		return
	needed_item = item_to_trade[item]
	cost_ = get_cost(needed_item) 
	if item ==Items.Cactus or item ==Items.Pumpkin or item == Items.Power:
		count = power(get_world_size(),2) *2 
	if item == Items.Bones:
		count = get_world_size()**2 * 4
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
		seeds_needed = 0
		if item_ == Items.Carrot:
			yield = (3 * (num_unlocked(Unlocks.Carrots) -1))
			seeds_needed = ((amount_of_this_item_needed - num_items(item)) // yield) +1
		trade_item(item_,seeds_needed)
		farm_item(item_ , amount_of_this_item_needed + current_num )
	trade(needed_item ,count)

			