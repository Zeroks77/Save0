def anum_items(item):
	return 155
	
item = Items.Carrot
costs = {Items.Carrot : 300}
amount_of_this_item_needed = costs[item] - num_items(item)
yield = return_current_yield_per_tile(item)
seeds_needed = (amount_of_this_item_needed // yield) +1break