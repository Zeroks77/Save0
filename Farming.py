def farm(want_to_have,till):
	if can_farm_sunflower(want_to_have/4):
		if not till: 
			till_field()
			till = True
		farm_sunflower(want_to_have)
	elif can_farm_maze(want_to_have):
		if till: 
			untill_field()
			till = False
		farm_maze()
	elif can_farm_pumpkin(want_to_have):
		if not till: 
			till_field()
			till = True
		farm_pumpkin(want_to_have)
	elif can_farm_carrot(want_to_have):
		if not till: 
			till_field()
			till = True
		farm_carrots(want_to_have)
	elif num_items(Items.Wood) < want_to_have:
		if till: 
			untill_field()
			till = False
		farm_wood(want_to_have)
	else:
		if till: 
			untill_field()
			till = False
		farm_hay(want_to_have)
		
def got_want_to_have(want_to_have) :
	return (num_items(Items.Hay) == want_to_have and 
		num_items(Items.Wood) == want_to_have and 
		num_items(Items.Carrot) == want_to_have and 
		num_items(Items.Pumpkin) == want_to_have and
		num_items(Items.Gold) == want_to_have and
		num_items(Items.Power) == want_to_have / 2)
	
	
	

	
	
	
				