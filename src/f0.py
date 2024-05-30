clear()move_to(0,0)
harvest()
plant(Entities.Bush)
set_farm_size(7)
while get_entity_type() == Entities.Bush and num_items(Items.Fertilizer) > 0:
	use_item(Items.Fertilizer)
navigate_maze(50)