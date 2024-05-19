def farm_item(i,amount_of_this_item_needed):
	while num_items(i) < amount_of_this_item_needed:	
		if num_items(item_to_trade[i]) != 0 or i == Items.Hay or i == Items.Wood or i == Items.Gold:
			if i == Items.Hay: 
				farm_hay()
			elif i == Items.Wood:
				farm_wood()
			elif i == Items.Carrot:
				farm_carrots()
			elif i == Items.Pumpkin:
				farm_pumpkin()
			elif i == Items.Gold:
				farm_maze()
			elif i == Items.Cactus:
				farm_cati()
			elif i == Items.Power:
				farm_sunflower()
			elif i == Items.Bones: 
				farm_dino()
		else:
			break

def farm_maze():
	move_to(0,0)
	harvest()
	plant(Entities.Bush)
	minFertilizer = power(get_world_size(), 4) * 3
	trade_item(Items.Fertilizer,minFertilizer)
	navigate_maze(500)
	harvest()
	till_field()
def farm_pumpkin():
	move_to(0,0)
	if get_entity_type() != None:
		clear_row(2) 
	pumpkin_measure()

def farm_sunflower():
	clear_grid()
	sunflower_measure()
def farm_carrots():
	if num_unlocked(Unlocks.Trees):
		plant_row(Items.Carrot,1)
	else: 
		plant_row(Items.Carrot,2)
	
def farm_wood():
	if num_unlocked(Unlocks.Trees):
		plant_row(Items.Wood,1)
	else: 
		plant_row(Items.Wood,2)
def farm_cati():
	clear_grid()
	plant_field(Items.Cactus)
	cactus_measure()
def farm_dino():
	clear_grid()
	dino()
def farm_hay():
	harvest_item(Items.Hay)