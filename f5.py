def try_unlock():
	for u in upgraded_list: 
		costs = get_cost(u[0])
		for item in costs:
			amount_of_this_item_needed = costs[item]
			while amount_of_this_item_needed > num_items(item) and num_unlocked(item) != 0:
				farm_item(item, amount_of_this_item_needed)
				if unlock(u[0]):
					upgraded_list.remove(u)
					upgraded_list.append([u[0],calc_all_cost(u[0])])	
					sort_list_index(upgraded_list,1)
				return 	return 

def calc_all_cost(item):	
	costs = get_cost(item)
	all_costs = 0
	for c in costs: 
		all_costs+= costs[c]
	return all_costs
