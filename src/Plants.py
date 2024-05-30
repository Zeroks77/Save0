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
	minFertilizer = power(get_world_size(), 3)
	trade_item(Items.Fertilizer,minFertilizer)
	move_to(0,0)
	harvest()
	navigate_maze(50)
	till_field()
def farm_pumpkin():	pumpkin_measure()
	
def farm_sunflower():
	clear_grid()
	sunflower_measure()

def farm_carrots():
	if num_unlocked(Unlocks.Polyculture) == 1:
		polyculture(Entities.Carrots)
	else:
		plant_row(Items.Carrot)
	
def farm_wood():
	harvest()
	if num_unlocked(Unlocks.Polyculture) == 1:
		polyculture(Entities.Tree)
	else:
		plant_row(Items.Wood)
	
def farm_cati(): 
	Cactus_Cycle()
	
def farm_dino():
	dino()
def farm_hay():
	if num_unlocked(Unlocks.Polyculture) == 1:
		polyculture(Entities.Grass)
	else:
		if num_unlocked(Unlocks.Plant) == 0:
			harvest_item(Items.Hay)
		else:
			plant_row(Items.Hay)