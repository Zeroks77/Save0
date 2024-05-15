def farm_item(i,amount_of_this_item_needed):
	while num_items(i) < amount_of_this_item_needed:	
		if i == Items.Hay: 
			tilled = farm_hay()
		elif i == Items.Wood:
			tilled = farm_wood()
		elif i == Items.Carrot:
			tilled = farm_carrots()
		elif i == Items.Pumpkin:
			tilled = farm_pumpkin()
		elif i == Items.Gold:
			tilled = farm_maze()
		elif i == Items.Cactus:
			tilled = farm_cati()
		elif i == Items.Bones: 
			tilled = farm_dino()

def farm_maze():
	move_to(0,0)
	plant(Entities.Bush)
	minFertilizer = power(get_world_size(), 2) * 3
	while get_entity_type() == Entities.Bush:
		trade_item(Items.Fertilizer)
		if num_items(Items.Fertilizer) > minFertilizer: 
			use_item(Items.Fertilizer)
		else:
			break
	maze_solve()
def farm_pumpkin():
	trade_item(Items.Pumpkin_Seed)
	initial_plant(Items.Pumpkin)
	pumpkin_measure()

def farm_sunflower():
	trade_item(Items.Power)
	initial_plant(Items.Power)
	sunflower_measure()
	
def farm_carrots():
	trade_item(Items.Carrot)
	initial_plant(Items.Carrot)
	farmgrid(Items.Carrot)
	
def farm_wood():
	initial_plant(Items.Wood)
	farmgrid(Items.Wood)
	
def farm_cati():
	trade_item(Items.Cactus)
	initial_plant(Items.Cactus)
	cactus_measure()
	
def farm_dino():
	trade_item(Items.Egg)
	initial_plant(Items.Bones)
	farmgrid(Items.Bones)
	
def farm_hay():
	if get_world_size() == 1: 
		harvest_item(Items.Hay)
	else:
		farmgrid(Items.Hay)