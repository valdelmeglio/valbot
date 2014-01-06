import rg

# the idea behind "assistance" is that when self is free, look for a nearby 1:1 engagement between robots and go help out
def should_assist(robot, game):
	for loc, other in game['robots'].items():
		if other.player_id != robot.player_id:
			if rg.wdist(other.location, robot.location) == 2:
				if len(get_neighboring_enemies(other, game)) > 0: # this enemy is "engaged" with my teammate
					if rg.dist(other.location, robot.location) == 2: # the 2 robots are on a line
						target_space = rg.toward(robot.location, other.location)
						if target_space not in game.robots:
							print 'assist!', target_space
							return ['move', target_space]
					else: # kitty corner, so need to check two target spaces
						0
	return None

def get_neighboring_enemies(robot, game):
	neighboring_enemies = []
	neighbors = rg.locs_around(robot.location)
	for loc, other in game['robots'].items():
		if loc in neighbors:
			if other.player_id != robot.player_id:
				neighboring_enemies.append(other.location)
	return neighboring_enemies

class Robot:
    def act(self, game):
        adjEnemyCount = 0 # adjacent enemy robots
        # if we're in the center, stay put
        if self.location == rg.CENTER_POINT:
            print 'guard!'
            return ['guard']

        # if there are enemies around, attack them
        for loc, bot in game.robots.iteritems():
            assist_action = should_assist(self, game)
    	    if (assist_action is not None): 
    	        return assist_action
    	        
            if bot.player_id != self.player_id:
                if rg.wdist(loc, self.location) == 1:
                    adjEnemyCount += 1
                if adjEnemyCount >= 3:
                    if self.hp <= adjEnemyCount * 9:
                        print 'suicide!'
                        return ['suicide']                    
                if rg.dist(loc, self.location) <= 1:
                    return ['attack', loc]

        # move toward the center
        return ['move', rg.toward(self.location, rg.CENTER_POINT)]