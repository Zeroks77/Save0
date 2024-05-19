def map_maze():
	x, y = get_pos_x(), get_pos_y()	grid = CreateGrid(get_world_size())
	treasure = ()
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			SetGridValue(x,y,grid, [None,None,None,None])
	while not Checked_Directions(grid):
		MoveDirection(grid)
		if get_entity_type() == Entities.Treasure:
			treasure = (x,y)
	#DebugMazeGrid(grid)
def Checked_Directions(grid):
	for row in grid: 
		for cell in row: 
			for d in cell: 
				if d == None:
					return False	return True
def MoveDirection(grid):
    x, y = get_pos_x(), get_pos_y()
	for i in range(len(dirs)):
		d = dirs[i][0]
		if(x+dirs[i][1]>=len(grid) or y+dirs[i][2]>=len(grid[x])):
			SetGridValue_(x,y,grid,d,False)			continue
		if(x+dirs[i][1]<0 or y+dirs[i][2]<0):
			SetGridValue_(x,y,grid,d,False)
			continue		# State if Move in Dir
		dir_explored=	GetGridValue_(x,y,grid,d)		# Next Move all Dir
		Next_Field_Move_List = GetGridValue(x+dirs[i][1],y+dirs[i][2],grid)
		This_Field_Move_List = GetGridValue(x,y,grid)
		count_this = has_1_None(This_Field_Move_List)
		count_next = has_1_None(Next_Field_Move_List)
		prev_check = not came_frome_here(x+dirs[i][1],y+dirs[i][2],grid,d)
		if dir_explored == None and (count_this  or prev_check):
			if (move(d)):
				x, y = get_pos_x(), get_pos_y()
				SetGridValue_(x-dirs[i][1],y-dirs[i][2],grid,d)
				break
		if dir_explored == None and prev_check:
			SetGridValue_(x,y,grid,d,False)
	
def came_frome_here(x,y,grid,d):
	dir = GetGridValue_(x,y,grid,OppositeDir[d])
	if dir == None:
		return False
	if dir == False:
		return False
	return  True
def has_1_None(dir_list):
	i = 0
	for d in dir_list:
		if d != None:
			i+=1
	return i == 3
def GetGridValue_(x, y, grid,d):
    return grid[x][y][dir_index[d]]
    
def SetGridValue_(x,y,grid,d,f = None):
	if f == None:
		grid[x][y][dir_index[d]] = d
    else: 
		grid[x][y][dir_index[d]] = False