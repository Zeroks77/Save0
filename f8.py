timed_reset()
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
	Items.Cactus : 8, 
	Items.Carrot : 3, 
	Items.Pumpkin: 8, 
	Items.Bones: 1, 
	Items.Power: 4,
	Items.Gold : 82
}
cost_scale = {
	Items.Wood : 1,
	Items.Hay : 1,
	Items.Carrot : 1.5, 
	Items.Pumpkin: 0.3, 
	Items.Gold : 0.75,
	Items.Cactus : 2, 
	Items.Bones: 3, 
	Items.Power: 2
}
till_ = {
	Items.Hay : False,
	Items.Carrot: True,
	Items.Pumpkin: True,
	Items.Power : True,
	Items.Cactus : True,
	Items.Gold : False,
	Items.Bones : True
}
for i in unlocks: 
	upgraded_list.append([i,calc_all_cost(i)])
while not unlock(Unlocks.Leaderboard):
	try_unlock()  
timed_reset()