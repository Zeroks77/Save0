def can_farm_sunflower(want_to_have):
	if num_items(Items.Power) > want_to_have:
		return False
	if num_items(Items.Sunflower_Seed) > get_seeds():
		return True
	if num_items(Items.Carrot) > want_to_have / 2:		
		trade(Items.Sunflower_Seed, get_seeds())
		return True 	
	return False
def can_farm_maze(want_to_have):
	if num_items(Items.Gold) > want_to_have:
		return False
	if num_items(Items.Fertilizer) > get_seeds():
		return True
	if num_items(Items.Pumpkin) > want_to_have / 2:		trade(Items.Fertilizer, get_seeds())
		return True 	return False

def can_farm_pumpkin(want_to_have):
	if num_items(Items.Pumpkin) > want_to_have:
		return False
	if num_items(Items.Pumpkin_Seed) > get_seeds():
		return True
	if num_items(Items.Carrot) > want_to_have / 2:		
		trade(Items.Pumpkin_Seed, get_seeds())
		return True 	
	return False

def can_farm_carrot(want_to_have):
	if num_items(Items.Carrot) > want_to_have:
		return False	if num_items(Items.Carrot_Seed) > get_seeds():
		return True
	if num_items(Items.Wood) > want_to_have / 2 and num_items(Items.Hay) >want_to_have / 2:		
		trade(Items.Carrot_Seed, get_seeds())
		return True 	
	return False
	
def get_seeds():
	worldsize = get_world_size() 
	return power(worldsize, 2) * 5