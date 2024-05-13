def grid_measure():
	measures = [] 
	check_positions = fill_with_board()
	while len(check_positions) != 0:
		pos = check_positions.pop()
		move_to(pos[0],pos[1])
		a = measure()
		if a != None:
			measures.append([[get_pos_x(), get_pos_y()], a])
		if can_harvest() == False:
			check_positions.insert(0,pos)
	while num_items(Items.Sunflower_Seed) > power(get_world_size()) * 2:
		quick_sort(list)
		
def random_list_index(list):	index = random() * len(list) // 1
	return list[index]
def sort_dim(list, index):
	quick_sort(list, 0, len(list) -1,index)
def quick_sort(list,  left, right, index):
	if(left > right):		return
	
	pivotPos = partition(list, left, right, index)
	quick_sort(list, left, pivotPos -1, index)
	quick_sort(list, pivotPos + 1, right, index)
	
def partition(list, left, right, index): 
	pivot = list[right][index]
	
	i = left
	j = right -1
	while i < j : 
		while list[i][index] < pivot:
			i+= 1
		while j > left and list[j][index] >= pivot:
			j-= 1
		if i < j: 
			element_swap(list, i, j)
			i+= 1
			j-= 1
	test = list[i][index]
	if i == j and list[i][index] < pivot:
		i+= 1
	if list[i][index] != pivot:
		element_swap(list, i, right)
	return i 

def element_swap(list, i, j):
	(list[i], list[j]) = (list[j], list[i])