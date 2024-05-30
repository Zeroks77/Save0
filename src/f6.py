def dino():
	move_to(0,0)
	use_item(Items.Egg)
	dino_type = measure()
	while not on_board_end():
		move_()
		use_item(Items.Egg)
	move_to(0,0)
	while not on_board_end():
		use_item(Items.Egg)	
		measure_ = measure()
		while dino_type != measure_ and measure_ != None:
			harvest()
			use_item(Items.Egg)
			measure_ = measure()
		move_()
	use_item(Items.Egg)
	move_()
	while dino_type != measure():
		harvest()
		use_item(Items.Egg)

	harvest()
	