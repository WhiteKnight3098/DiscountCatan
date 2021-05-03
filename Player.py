class Player():
  def __init__(self, name):
    self.name = name
    self.player_hand = []  #dev cards
    self.resources = []  #Resource only
    self.stone = []
    self.clay = []
    self.wheat = []
    self.sheep = []
    self.wood = []

  # Resource Collection and Trades
  def addResource(self, diceroll, random_values, tiles):
    indexValues = []
    for number in range(len(random_values)):
      if diceroll == random_values[number]:
        indexValues.append(number)
    self.resources.append(tiles[number])
    pass

  def returnResources(self):
    for index in range(len(self.resources)):
      if self.resources[index] == "Stone":
        self.stone.append(index)
      elif self.resources[index] == "Clay":
        self.clay.append(index)
      elif self.resources[index] == "Wheat":
        self.wheat.append(index)
      elif self.resources[index] == "Sheep":
        self.sheep.append(index)
      elif self.resources[index] == "Wood":
        self.wood.append(index)

  def spendResource():
    pass

  def loseResource():
    pass

  def stealResource():
    pass

  # Purchases and Builds
  def layRoad(self, clay, wood):
    pass

  def buildSettlement(self, clay, wood, wheat, sheep):
    pass

  def upgradeCity(self, wheat, stone): #2 wheat, 3 stone
    pass

  def PurchaseCard(self, Sheep, Wheat, Stone):
    if Sheep and Wheat and Stone:
      self.player_hand.append(Deck.drawCard())

  # Development Card Methods
  def PlayCard(self):
    pass

  # Debug Methods
  def ShowHand(self):
    for card in self.player_hand:
      Card.showCard()

  def ShowResources(self):
    holding = []
    for resource in self.resources:
      holding.append(resource)
    print(holding)
