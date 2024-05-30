unlocks = [
	Unlocks.Leaderboard,
	Unlocks.Dinosaurs,
	Unlocks.Cactus,
	Unlocks.Sunflowers,
	Unlocks.Mazes,
	Unlocks.Fertilizer,
	Unlocks.Pumpkins,
	Unlocks.Trees,
	Unlocks.Carrots,
	Unlocks.Plant, 
	Unlocks.Expand,
	Unlocks.Speed,
	Unlocks.Grass
]

item_to_unlock = {
	Items.Hay : Unlocks.Grass,
	Items.Wood : Unlocks.Trees,
	Items.Carrot: Unlocks.Carrots,
	Items.Pumpkin: Unlocks.Pumpkins,
	Items.Power : Unlocks.Sunflowers,
	Items.Cactus : Unlocks.Cactus,
	Items.Gold : Unlocks.Mazes,
	Items.Bones : Unlocks.Dinosaurs

}
item_to_trade = {
	Items.Gold : Items.Fertilizer,
	Items.Wood : Items.Wood,
	Items.Hay : Items.Hay,
	Items.Cactus : Items.Cactus_Seed, 
	Items.Carrot : Items.Carrot_Seed, 
	Items.Pumpkin: Items.Pumpkin_Seed, 
	Items.Bones: Items.Egg, 
	Items.Power: Items.Sunflower_Seed,
	Items.Fertilizer : Items.Fertilizer
}
item_to_entity = {
	Items.Carrot:Entities.Carrots,
	Items.Pumpkin:Entities.Pumpkin,
	Items.Power:Entities.Sunflower,
	Items.Cactus:Entities.Cactus,
	Items.Hay : Entities.Grass
}

cost_scale = {
	Items.Wood : 0.5,
	Items.Hay : 0.5,
	Items.Carrot : 1, 
	Items.Pumpkin: 0.7, 
	Items.Gold : 1,
	Items.Cactus : 1, 
	Items.Bones: 0.5, 
	Items.Power: 1
}
upgraded_list = [
Unlocks.Grass,
Unlocks.Speed,
Unlocks.Plant,
Unlocks.Expand,
Unlocks.Grass,
Unlocks.Speed,
Unlocks.Expand,
Unlocks.Grass,
Unlocks.Grass,
Unlocks.Carrots,
Unlocks.Speed,
Unlocks.Trees,
Unlocks.Expand,
Unlocks.Pumpkins,
Unlocks.Expand,
Unlocks.Expand,
Unlocks.Grass,
Unlocks.Trees,
Unlocks.Carrots,
Unlocks.Carrots,
Unlocks.Carrots,
Unlocks.Polyculture,
Unlocks.Carrots,
Unlocks.Grass,
Unlocks.Grass,
Unlocks.Trees,
Unlocks.Speed,
Unlocks.Speed,
Unlocks.Speed,
Unlocks.Speed,
Unlocks.Pumpkins,
Unlocks.Pumpkins,
Unlocks.Fertilizer,
Unlocks.Expand,
Unlocks.Speed,
Unlocks.Speed,
Unlocks.Speed,
Unlocks.Mazes,
Unlocks.Mazes,
Unlocks.Mazes,
Unlocks.Mazes,
Unlocks.Sunflowers,
Unlocks.Cactus,
Unlocks.Cactus,
Unlocks.Cactus,
Unlocks.Expand,
Unlocks.Expand,
Unlocks.Dinosaurs,
Unlocks.Dinosaurs,
Unlocks.Leaderboard
]
timed_reset()
op = get_op_count()
#for i in unlocks: 
	#upgraded_list.append([i,calc_all_cost(i), get_cost(i)])
while num_unlocked(Unlocks.Leaderboard) == 0:
	try_unlock()  
timed_reset()