# DiscountCatan
This is a port of the popular game Catan from the Real Life engine to Python.


Key Components of Catan:

  2 dice

  Robber   (Starts on the Desert hex)
  
  4 teams
  
  19 Hexes
    4 Sheep fields
    4 Woodlands
    4 Croplands
    3 Mountain mines
    3 Clay pits
    1 desert
    
  Numbers for Hexes
    2
    3 x2
    4 x2
    5 x2
    6 x2
    8 x2
    9 x2
    10 x2
    11 x2
    12
    
  Player pieces
    4 Cities  (worth 2 VP)
    5 Settlement  (worth 1 VP)
    15 Roads
    
  Development Cards (Dev Cards)
    14 Knights
    5 Victories ( Chapel, University, Market, Palace, Library ) (+1 VP)
    2 Monopoly (All resources getter)
    2 Year of plenty (Take any 2 resources from the bank
    2 Road building (Place 2 new roads
    
  Bonus Points (+2)
    Longest Road (minimum 5 road segments)
    Largest Army
    
  Building Costs:
    Road = 1 clay + 1 wood
    Settlement = 1 clay + 1 wood + 1 wheat + 1 sheep
    City = 2 wheat + 3 stone
    Dev Card = 1 sheep + 1 wheat + 1 stone
    
  Ports (in order of appearance):
    2 sheep = 1 any
    3 same = 1 any 
    3 same = 1 any
    2 clay = 1 any
    2 wood = 1 any
    3 same = 1 any
    2 wheat = 1 any
    2 rocks = 1 any
    3 same = 1 any
    
  Turn Order:
    1. Roll the dice and Resolve events (collect resources or move robber)
    2. Trade resources or use ports owned
    3. Use Dev Cards
    4. Purchase and Build
    
  Key runtime things:
    1. Settlements must be built at least 2 road spaces away from another settlment/city
    2. Settlements are built and later may be upgraded to a city
    3. Robber gets moved on the roll of a 7 or the use of a knight. This triggers the robbing of a player on that hex. Anyone with 7+ cards discards half (on the roll only)
    4. Robbers block resources from generating on the hex in which in resides
    5. Development cards must be held 1 turn before played
    6. All building placements and purchases are final
    7. 10 Victory Points (VP) to win the game!
    8. Original placement goes through everyone twice, once forward, then once backward
    9. ALL PLAYERS START WITH THE RESOURCES FROM THEIR SECOND HOUSE PLACEMENT
    
  
  
  
