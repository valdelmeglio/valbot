import rg

class Robot:
    def act(self, game):
        adjEnemyCount = 0 # adjacent enemy robots
        # if we're in the center, stay put
        if self.location == rg.CENTER_POINT:
            return ['guard']

        # if there are enemies around, attack them
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id:
                if rg.wdist(loc, self.location) == 1:
                    adjEnemyCount += 1
                if adjEnemyCount >= 3:
                    if self.hp <= adjEnemyCount * 9:
                        return ['suicide']                    
                if rg.dist(loc, self.location) <= 1:
                    return ['attack', loc]

        # move toward the center
        return ['move', rg.toward(self.location, rg.CENTER_POINT)]
        
