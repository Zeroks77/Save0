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