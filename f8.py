unlocks = [
	Unlocks.Grass,
	Unlocks.Speed,
	Unlocks.Expand,
	Unlocks.Plant, 
	Unlocks.Carrots,
	Unlocks.Trees,
	Unlocks.Pumpkins,
	Unlocks.Sunflowers,
	Unlocks.Fertilizer,
	Unlocks.Mazes,
	Unlocks.Cactus,
	Unlocks.Dinosaurs,
	Unlocks.Leaderboard
]
upgraded_list = []
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
	Items.Cactus:Entities.Cactus
}
yield = {
	Items.Cactus : get_world_size() **3, 
	Items.Carrot : 3, 
	Items.Pumpkin: get_world_size() **3, 
	Items.Bones: get_world_size()**2 * 4, 
	Items.Power: 14,
	Items.Gold : 350
}
cost_scale = {
	Items.Wood : 0.5,
	Items.Hay : 0.5,
	Items.Carrot : 1, 
	Items.Pumpkin: 0.7, 
	Items.Gold : 1,
	Items.Cactus : 1, 
	Items.Bones: 0.7, 
	Items.Power: 3
}
timed_reset()
for i in unlocks: 
	upgraded_list.append([i,calc_all_cost(i), get_cost(i)])
while num_unlocked(Unlocks.Leaderboard) == 0:
	try_unlock()  
timed_reset()