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
for i in unlocks: 
	upgraded_list.append([i,calc_all_cost(i)])
while not unlock(Unlocks.Leaderboard):
	farm() 
timed_reset()