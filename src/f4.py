def polyculture(Entity):
	grid = {}
	move_to(0,0)
	def get_Entity(x,y):
		if (x,y) in grid:
			return grid[(x,y)]
		if Entity == Entities.Tree:
			if x+y % 2 == 0 :
				return Entities.Tree
			else : 
				return Entities.Bush
		else :	
			return Entity  
		def tile_():
		x,y = get_pos_x(),get_pos_y()
		while not can_harvest() and get_entity_type() != None:
			water()
		harvest()
		till_()
		e = get_Entity(x,y)
		plant(get_Entity(x,y))
		water()
		com = get_companion()
		if com == None:
			return		else: 
			if not ((com[1],com[2]) in grid):
				grid[(com[1],com[2])]= com[0]
			else: 
				return
					
	while not on_board_end():
		tile_()
		move_()
				
	
