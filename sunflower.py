def sunflower_measure():
	most_pedals = [0,0,0] 
	initial_plant(Items.Power)
	harvested = False
	move_to(0,0)
	world_size = get_world_size()
	seeds = num_items(Items.Sunflower_Seed)
	check_positions = fill_with_board()
	while not seeds < power(get_world_size(),2) * 2: 
		if  len(check_positions) == 0:
			if a < world_size // 1.2: 
				harvest()
				break
			move_to(most_pedals[0], most_pedals[1])
			harvest_item(Items.Power)
			most_pedals = [0,0,0] 
			check_positions = fill_with_board()			
			move_to(0,0)
		pos = check_positions.pop()
		move_to(pos[0],pos[1])
		if can_harvest() == False:
			check_positions.insert(0,pos)
		a = measure()
		if a != None and a > most_pedals[2]:
			most_pedals = [get_pos_x(),get_pos_y(),a]
		if a == None: 
			move_to(0,0)
			break
		