def farm_item(i,amount_of_this_item_needed):
	tilled = False
	while num_items(i) < amount_of_this_item_needed:	
		if i == Items.Hay: 
			tilled = farm_hay(tilled)
		elif i == Items.Wood:
			tilled = farm_wood(tilled)
		elif i == Items.Carrot:
			tilled = farm_carrots(tilled)
		elif i == Items.Pumpkin:
			tilled = farm_pumpkin(tilled)
		elif i == Items.Gold:
			tilled = farm_maze(tilled)
		elif i == Items.Cactus:
			tilled = farm_cati(tilled)
		elif i == Items.Bones: 
			tilled = farm_dino(tilled)


def farm_maze(tilled):
	if tilled: 
		tilled = False
		untill_field()
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
	return tilled
def farm_pumpkin(tilled):
	if not tilled: 
		tilled = True
		till_field()
	trade_item(Items.Pumpkin_Seed)
	initial_plant(Items.Pumpkin)
	pumpkin_measure()
	return tilled

def farm_sunflower(tilled):
	if not tilled: 
		tilled = True
		till_field()
	trade_item(Items.Power)
	initial_plant(Items.Power)
	sunflower_measure()
	return tilled
	
def farm_carrots(tilled):
	if not tilled: 
		tilled = True
		till_field()
	trade_item(Items.Carrot)
	initial_plant(Items.Carrot)
	farmgrid(Items.Carrot)
	return tilled
	
def farm_wood(tilled):
	initial_plant(Items.Wood)
	farmgrid(Items.Wood)
	return tilled
	
def farm_cati(tilled):
	if not tilled: 
		tilled = True
		till_field()
	trade_item(Items.Cactus)
	initial_plant(Items.Cactus)
	cactus_measure()
	return tilled
	
def farm_dino(tilled):
	if tilled: 
		tilled = False
		untill_field()
	trade_item(Items.Egg)
	initial_plant(Items.Bones)
	farmgrid(Items.Bones)
	return tilled
	
def farm_hay(tilled):
	if tilled: 
		tilled = False
		untill_field()
	if get_world_size() == 1: 
		harvest_item(Items.Hay)
	else:
		farmgrid(Items.Hay)
	return tilled