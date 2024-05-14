def farm(want_to_have,tilled):
	if can_farm_sunflower(want_to_have/4):
		if not tilled: 
			till_field()
			tilled = True
		farm_sunflower()
	elif can_farm_dino(want_to_have):
		if tilled:
			untill_field()
			tilled = False
		
	elif can_farm_cacti(want_to_have): 
		if not tilled: 
			till_field()
			tilled = True
		farm_cati()
	elif can_farm_maze(want_to_have):
		if tilled: 
			untill_field()
			tilled = False
		farm_maze()
	elif can_farm_pumpkin(want_to_have):
		if not tilled: 
			till_field()
			tilled = True
		farm_pumpkin()
	elif can_farm_carrot(want_to_have):
		if not tilled: 
			till_field()
			tilled = True
		farm_carrots()
	elif num_items(Items.Wood) < want_to_have:
		if tilled: 
			untill_field()
			tilled = False
		farm_wood()
	elif num_items(Items.Hay) < want_to_have:
		if tilled: 
			untill_field()
			tilled = False
		farm_hay()	
	return tilled
	
		
def got_want_to_have(want_to_have) :
	return (num_items(Items.Hay) == want_to_have and 
		num_items(Items.Wood) == want_to_have and 
		num_items(Items.Carrot) == want_to_have and 
		num_items(Items.Pumpkin) == want_to_have and
		num_items(Items.Gold) == want_to_have and
		num_items(Items.Power) == want_to_have / 2)
	
	
	

	
	
	
				