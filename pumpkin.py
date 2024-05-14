def pumpkin_measure():
	move_to(0,0)
	check_positions = fill_with_board()
	while len(check_positions) != 0:
			if num_items(Items.Pumpkin_Seed) == 0:
				check_positions = []
				break
			pos = check_positions.pop()
			move_to(pos[0],pos[1])
			if get_entity_type() == None:
				check_positions.insert(0,pos)
				plant(Entities.Pumpkin)
			if not can_harvest():
				check_positions.insert(0,pos)
	harvest_item(Items.Pumpkin)