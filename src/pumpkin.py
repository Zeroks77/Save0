def pumpkin_measure():
	check_positions = fill_with_board()
	while len(check_positions) != 0:
			if num_items(Items.Pumpkin_Seed) == 0:
				check_positions = []
				break
			pos = check_positions.pop()
			move_to(pos[0],pos[1])
			e = get_entity_type()  
			if e != Entities.Pumpkin:
				harvest()
				check_positions.insert(0,pos)
				till_()
				plant(Entities.Pumpkin)
				water()
			if  e == None:
				check_positions.insert(0,pos)
				till_()
				plant(Entities.Pumpkin)
				water()
			if not can_harvest():
				check_positions.insert(0,pos)
	harvest()

def fertilized_pumpkin_measure():
	if num_items(Items.Fertilizer) == 0:
		return False
	move_to(0,0)
	while not on_board_end(): 
		if get_entity_type() != Entities.Pumpkin:
			harvest()
		plant(Entities.Pumpkin)
		use_item(Items.Fertilizer)
		while not can_harvest():
			if num_items(Items.Fertilizer) > 0 or trade(Items.Fertilizer):
				plant(Entities.Pumpkin)
				use_item(Items.Fertilizer)
			else: 
				return False
		move_()
	plant(Entities.Pumpkin)
	use_item(Items.Fertilizer)
	while not can_harvest():
		plant(Entities.Pumpkin)
		use_item(Items.Fertilizer)
	harvest()
	return True