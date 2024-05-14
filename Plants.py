def farm_maze():
	move_to(0,0)
	plant(Entities.Bush)
	minFertilizer = power(get_world_size(), 2) * 3
	while get_entity_type() == Entities.Bush:
		if num_items(Items.Fertilizer) > minFertilizer: 
			use_item(Items.Fertilizer)
		else:
			break
	maze_solve()
def farm_pumpkin():
	initial_plant(Items.Pumpkin)
	pumpkin_measure()

def farm_sunflower():
	initial_plant(Items.Power)
	sunflower_measure()

def farm_carrots():
	initial_plant(Items.Carrot)

def farm_wood():
	initial_plant(Items.Wood)
	farmgrid(Items.Wood)
	
def farm_cati():
	initial_plant(Items.Cactus)
	cactus_measure()
	
def farm_dino():
	initial_plant(Items.Bones)
	farmgrid(Items.Bones)
	
def farm_hay():
	initial_plant(Items.Hay)
	farmgrid(Items.Hay)