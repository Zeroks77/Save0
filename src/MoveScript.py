def move_(): 
	y = get_pos_y()
	world = get_world_size() -1
	if y < world :
		move(North)
	else:
		move(East)
		move(North)
		
def debug(dir): 
	quick_print(get_pos_x(), get_pos_y())
	move(dir)
	
def move_to(x,y):
    def half_mod(x, n):
        return (x + n // 2) % n - n // 2

    n = get_world_size()
    x = half_mod(x - get_pos_x(), n)
    y = half_mod(y - get_pos_y(), n)

    for i in range(abs(x)):
        if x > 0:
            move(East)
        else:
            move(West)

    for i in range(abs(y)):
        if y > 0:
            move(North)
        else:
            move(South)


		