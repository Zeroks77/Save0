
move_to(0,0)
harvest()
plant(Entities.Bush)
minFertilizer = power(get_world_size(), 2) * 3
while get_entity_type() == Entities.Bush and num_items(Items.Fertilizer) > 0:
	use_item(Items.Fertilizer)
if get_entity_type() == Entities.Hedge:
	maze_solve()