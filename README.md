valbot
======


The AI implementation for a robot game (http://robotgame.org).

#Rules
In robot game, you write programs to control robots that fight for you. The game is played on a 19x19 grid.
![My image](http://robotgame.org/static/rules1.png)

Dark squares represent where you can't walk. As you can see, this effectively creates a circle arena where your robots fight.

The green squares represent spawn points. Every 10 turns, a batch of 5 robots will spawn at random spawn points for each player, and any robot still standing on a spawn point will die.

Each robot starts out with 50 HP.

Robots can generally act (move, attack, etc.) on the squares one above, left, right, and below it—its adjacent squares.

Each turn, every robot can take one action:

Move into an adjacent square. If there's already a robot there, or if another robot tries to move into the same square, both robots will lose 5 HP as collision damage, and the move(s) won't happen. On the other hand, if a robot tries to move into a square with a robot already there, but that robot successfully moves out the same turn, both robots will move.

Four robots in a square, all moving clockwise, will move, as will any number of robots that move in a circle.

* Attack an adjacent square. If there is a robot in that square at the end of the turn—i.e. a robot stayed there or successfully moved into that square—that robot will lose between 8 and 10 HP as attack damage.

* Suicide. The robot will die, dealing 15 to any robots in adjacent squares at the end of the turn.

* Guard. The robot will stay put, take half damage from attacks and suicides, and take no damage from collisions.

There is no friendly damage in this game. Collisions, attacks, and suicides will only damage the opponent.

Whoever has more robots left after 100 turns wins.

=======
The AI implementation for a robot game (http://robotgame.org)