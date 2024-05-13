def Pumpkin_test():
	full_grown = False
	world_size = get_world_size()
	while full_grown == False:
		for i in range(world_size):
			for j in range(world_size):
				if get_entity_type() != Entities.Pumpkin:
					trade(Items.Pumpkin_Seed)
					plant(Entities.Pumpkin)
				move(North)
			move(East)
		positions = []
		full_grown = True
		for i in range(world_size):
			for j in range(world_size):
				positions.append([get_pos_x,get_pos_y,can_harvest()])
				move(North)
			move(East)
		for item in positions: 
			if not item[2]:
				full_grown = False
	harvest()