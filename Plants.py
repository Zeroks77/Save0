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
	minFertilizer = power(get_world_size(), 2) * 3
	trade_item(Items.Fertilizer,minFertilizer)
	while get_entity_type() == Entities.Bush and num_items(Items.Fertilizer) > 0:
		use_item(Items.Fertilizer)
	if get_entity_type() == Entities.Hedge:
		maze_solve()
	if get_entity_type() == Entities.Treasure:
		harvest()
	till_field()
def farm_pumpkin():
	clear_row(2) 
	plant_field(Items.Pumpkin)
	pumpkin_measure()

def farm_sunflower():
	clear_grid()
	sunflower_measure()
def farm_carrots():
	plant_row(Items.Carrot,2)
	
def farm_wood():
	plant_row(Items.Wood,2)
def farm_cati():
	clear_grid()
	plant_field(Items.Cactus)
	cactus_measure()
def farm_dino():
	clear_grid()
	plant_field(Items.Bones)
def farm_hay():
	harvest_item(Items.Hay)