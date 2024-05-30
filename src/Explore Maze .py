def navigate_maze(times = -1):
    directions = {
        North: [West, East, South],
        East: [North, South, West],
        South: [East, West, North],
        West: [South, North, East]
    }
	NUMBER_OF_TILES = get_world_size() ** 2
	def buy(item, amount = -1, force = False):
		if not item:
			quick_print("No item id provided")
		if amount == -1:
			amount = NUMBER_OF_TILES
    
		count = num_items(item)
		if count > amount and not force:
			return True
		trade(item, amount)
    
		if count == num_items(item):
			quick_print("Could not purchase item")
			return False
		return True
    def replant():
        if get_entity_type() not in [Entities.Bush, Entities.Hedge]:
            plant(Entities.Bush)
        return get_entity_type() == Entities.Hedge or fertilize(Entities.Bush)
    
    def fertilize(entity):
        num = 0
        while get_entity_type() == entity:
            if buy(Items.Fertilizer) and num < 50:
                use_item(Items.Fertilizer)
            else:
                return False
            num += 1
        return True

	def vector_subtract(v1, v2):
		x = v1[0] - v2[0]
		y = v1[1] - v2[1]
		return {
        	x > 0 and East or West: abs(x),
        	y > 0 and North or South: abs(y)
    	}

	def get_priority(dict, index):
		if len(dict[index]) == 0:
			index += 1
		return dict[index].pop(), index
    
    def seek():
        game_data = {
            'next': None,
            'facing': North,
            'grid': {},
            'stop': False,
            'iterations': times >= 0 and times or 250
        }
        
        def insert_or_update(start, exit, direction):
            if not start in game_data['grid']:
                game_data['grid'][start] = {}
            game_data['grid'][start][exit] = direction
		def here():
			return (get_pos_x(),get_pos_y())
        def hug_wall():
            start = here()
            last_facing = game_data['facing']
            if move(directions[last_facing][0]):
                game_data['facing'] = directions[last_facing][0]
            elif move(last_facing):
                pass
            elif move(directions[last_facing][1]):
                game_data['facing'] = directions[last_facing][1]
            else:
                move(directions[last_facing][2])
                game_data['facing'] = directions[last_facing][2]
            end = here()
            insert_or_update(start, end, game_data['facing'])
            insert_or_update(end, start, directions[game_data['facing']][2])
        
		def scout():
            while len(game_data['grid']) < NUMBER_OF_TILES:
                hug_wall()
                if get_entity_type() == Entities.Treasure:
                    game_data['next'] = here()

        def beeline(to):
            v = vector_subtract(to, here())
            
            for i in v:
                for j in range(v[i]):
                    from = here()
                    if move(i):
                        to = here()
                        insert_or_update(from, to, i)
                        insert_or_update(to, from, directions[i][2])
                    else:
                        return False
            return True
            
        def dijkstra(end):
            queue = {}
            came_from = {}
            cumulative = {}
            
            start = here()
            index = 0
            queue[index] = [end]
            came_from[end] = None
            cumulative[end] = index
            
            def step(where):
                if where in came_from and came_from[where]:
                    move(game_data['grid'][where][came_from[where]])
                return where
            
            while not len(queue) == 0:
                current, index = get_priority(queue, index)
                
                for next in game_data['grid'][current]:
                    new_cost = cumulative[current] + 1
                    if next not in cumulative or new_cost < cumulative[next]:
                        cumulative[next] = new_cost
                        if new_cost not in queue:
                            queue[new_cost] = []
                        queue[new_cost].append(next)
                        came_from[next] = current
                
                if current == start:
                    break
            
            while step(here()) != end:
                pass
                
            return True
		def smart_seek():
                 #first time grid
            scout()
            
            while game_data['iterations'] > 0:
                if game_data['next'] == None:
                    clear()					game_data['iterations'] = 0
					game_data['stop'] = True
					break
                if beeline(game_data['next']) or dijkstra(game_data['next']):
                    game_data['iterations'] -= 1
                else:
                    game_data['stop'] = True
                    return
                
                if game_data['iterations'] > 0:
                    game_data['next'] = measure()
                    if not fertilize(Entities.Treasure):
						harvest()	
						game_data['iterations'] = 0
						game_data['stop'] = True
						break
                else:
                    harvest()
            
            harvest()
            game_data['stop'] = True
            

		while not game_data['stop']:
            smart_seek()
    
    harvest()
    replant()
    seek()