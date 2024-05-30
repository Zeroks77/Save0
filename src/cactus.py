def Cactus_Cycle(a = 1):
	Size = get_world_size()
	if num_items(Items.Cactus_Seed) < Size * Size: 
		return
	for i in range(a):
		Cacti_Sort = 1
		Cactus_Cycle_Count = Size
		for i in range(Size):
			for i in range(Size):
				plant(Entities.Cactus)
				move(North)
			move(East)
		while Cacti_Sort > 0:
			Cacti_Sort = 0
			for i in range(Size):
				for i in range(Size):
					if Cactus_Cycle_Count > get_pos_x():
						if measure() > measure(North) and get_pos_y() != Size - 1:
							swap(North)
							Cacti_Sort = Cacti_Sort + 1
						if measure() > measure(East) and get_pos_x() != Size - 1:
							swap(East)
							Cacti_Sort = Cacti_Sort + 1
						if measure() < measure(South) and get_pos_y() != 0:
							swap(South)
							Cacti_Sort = Cacti_Sort + 1
						if measure() < measure(West) and get_pos_x() != 0:
							swap(West)
							Cacti_Sort = Cacti_Sort + 1
					move(North)
				move(East)
			Cactus_Cycle_Count -= 1
	harvest()
