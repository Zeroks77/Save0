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
	minFertilizer = power(get_world_size(), 4)
	trade_item(Items.Fertilizer,minFertilizer)
	move_to(0,0)
	harvest()
	navigate_maze(500)
	till_field()
def farm_pumpkin():
	move_to(0,0)
	min_fet = get_world_size()**2 *2
	clear_row(1) 
	if num_unlocked(Items.Fertilizer) == 1:
		if not fertilized_pumpkin_measure():
			pumpkin_measure()
	else: 		pumpkin_measure()
	

def farm_sunflower():
	clear_grid()
	sunflower_measure()

def farm_carrots():
	if num_unlocked(Unlocks.Expand) > 5:
		plant_row(Items.Carrot,1, True)
	else: 
		plant_row(Items.Carrot,1)
	
def farm_wood():
	harvest(Items.Wood)
	
	
	if num_unlocked(Unlocks.Expand) > 5:
		plant_row(Items.Wood,1, True)
	else:		plant_row(Items.Wood,1)
	
def farm_cati():
	plant_field(Items.Cactus)
	cactus_measure()
def farm_dino():
	dino()
def farm_hay():
	harvest_item(Items.Hay)