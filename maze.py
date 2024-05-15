def maze_solve():
    dirs = [North, East, South, West]
    dir_change = { True: 3, False: 1}
    dir = 0
    while get_entity_type() != Entities.Treasure:
        dir = (dir + dir_change[move(dirs[dir])]) % 4
	harvest()


