def try_unlock():
	for u in upgraded_list:
		#if u[0] == Unlocks.Fertilizer and num_unlocked(u[0]) > 0 or  u[0] == Unlocks.Plant and num_unlocked(u[0]) > 0 :
			#pgraded_list.remove(u)
			#continue
		#if u[1] == 0 or num_unlocked(u[0]) > 6 and u[0] != Unlocks.Expand:
			#upgraded_list.remove(u)
			#continue 
		costs = get_cost(u)
		if num_unlocked(u) == 2 and u == Unlocks.Cactus:
			trade_item(Items.Pumpkins,seeds_needed)
			prep(item)
			farm_item(Items.Gold, 35000)
		while not unlock(u):
			for item in costs:
			#if not can_unlock(item) or num_unlocked(item) == 0:
				#break
			#if num_unlocked(item_to_unlock[item]) < 2 and (item != Items.Bones and item != Items.Wood and item != Items.Pumpkin and item != Items.Hay and item != Items.Carrot):
				#break
				farm_power_check()
				amount_of_this_item_needed = costs[item] 
				if item != Items.Bones or item != Items.Pumpkin or item !=Items.Cactus or item !=Items.Power:
					seeds_needed = ((amount_of_this_item_needed - num_items(item)) // return_current_yield_per_tile(item)) +1
				trade_item(item,seeds_needed)
				farm_item(item, amount_of_this_item_needed)
		if u == Unlocks.Expand:			till_field() 
				#upgraded_list.pop(0)
				#apend([u[0],calc_all_cost(u[0]),get_cost(u[0])])	
				#sort_list_index(upgraded_list,1)

def farm_power_check():
	if num_unlocked(Unlocks.Expand) < 4: 
		return
	unlock_level = num_unlocked(item_to_unlock[Items.Power])
	world = get_world_size()	if unlock_level > 0 and num_items(Items.Power) < world ** 2 * 2:
		item = Items.Power
		trade_item(item, 0)
		prep(item)
		farm_sunflower()		
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
