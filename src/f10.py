harvest()
item_to_entity = {
	Items.Carrot:Entities.Carrots,
	Items.Pumpkin:Entities.Pumpkin,
	Items.Power:Entities.Sunflower,
	Items.Cactus:Entities.Cactus,
	Items.Hay : Entities.Grass
}a = get_time()
b = num_items(Items.Cactus)Cactus_Cycle(1)quick_print("Time To Farm", num_items(Items.Cactus) -b ,"Cacti", get_time() - a, "seconds" )