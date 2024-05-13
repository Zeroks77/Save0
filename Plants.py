def farm_maze():
	move_to(0,0)
	plant(Entities.Bush)
	minFertilizer = power(get_world_size(), 2) * 3
	while get_entity_type() == Entities.Bush:
		if num_items(Items.Fertilizer) > minFertilizer: 
			use_item(Items.Fertilizer)
		else:
			break
	navigate_maze()