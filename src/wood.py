def woodgrid():	
	if ((get_pos_x() + get_pos_y()) % 2 == 0) :
		plant(Entities.Tree)	
	else:		
		plant(Entities.Bush)