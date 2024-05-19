def try_unlock():
	sort_list_index(upgraded_list,1)
	for u in upgraded_list:
		if u[1] == 0 or num_unlocked(u[0]) > 5 and u[0] != Unlocks.Expand:
			upgraded_list.remove(u)
			continue 
		costs = u[2]
		if num_unlocked(item_to_unlock[Items.Power]) > 2 and num_items(Items.Power) < get_world_size() ** 4:
			item = Items.Power
			trade_item(item,get_world_size() **3)
			prep(item)
			farm_item(item, get_world_size() ** 3)
		for item in costs:
			if num_unlocked(item_to_unlock[item]) < 3 and (item != Items.Wood and item != Items.Pumpkin and item != Items.Hay and item != Items.Carrot):
				break
			if not can_unlock(item) or num_unlocked(item) == 0:
				break
			amount_of_this_item_needed = costs[item] 
			seeds_needed = ((amount_of_this_item_needed - num_items(item)) // return_current_yield_per_tile(item)) +1
			trade_item(item,seeds_needed)
			prep(item)
			farm_item(item, amount_of_this_item_needed)
			if unlock(u[0]):
				if u[0] == Unlocks.Expand:					till_field() 
				upgraded_list.remove(u)
				upgraded_list.append([u[0],calc_all_cost(u[0]),get_cost(u[0])])
				return

				
def return_current_yield_per_tile(item):
	if item == Items.Hay or item == Items.Wood :
		return 1
	yield_of_item = yield[item]
	unlock_level = num_unlocked(item_to_unlock[item])
	if unlock_level > 0:
		yield_of_item = yield_of_item * unlock_level
	return yield_of_item 
	
def can_unlock(item) : 
	if item == Items.Wood or item == Items.Hay:
		return True
	costs = get_cost(item_to_unlock[item])
	unlock_possible = True
	if costs == None:
		return True
	for item in costs:
		unlock = unlock_possible and is_unlocked(item)
	return unlock

def is_unlocked(item):
	if item == Items.Wood or item == Items.Hay:
		return True
	if num_unlocked(item_to_unlock[item]) != 0:
		return True
	return False
				
def prep(item): 
	if item == Items.Wood:
		return
	move_to(0,0)
	if item == Items.Hay: 
		if get_ground_type() == Grounds.Soil: 
			till()
		return
	else: 
		if get_ground_type() == Grounds.Turf: 
			till()
		return	
		
def calc_all_cost(item):	
	costs = get_cost(item)
	if costs == None:
		return 0
	all_costs = 0
	for c in costs: 
		all_costs += (costs[c] * cost_scale[c]) // 1	unlock_level = num_unlocked(item)
	if unlock_level > 0:
		all_costs = (all_costs * (unlock_level/2)) // 1
	return all_costs
