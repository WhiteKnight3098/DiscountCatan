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
    print("Stone = {}, Clay = {}, Wheat = {}, Sheep = {}, Wood = {}".format(len(self.stone),len(self.clay),len(self.wheat),len(self.sheep),len(self.wood)))

  def spendResource(self, purchase):
    if purchase == "road":
      if len(self.wood) >= 1 and len(self.clay) >= 1:
        layRoad()
      else:
        print("Sorry! Not enough resources")

    elif purchase == "settlement":
      if len(self.wood) >= 1 and len(self.clay) >= 1 and len(self.sheep) >= 1 and len(self.wheat) >= 1:
        buildSettlement()
      else:
        print("Sorry! Not enough resources")

    elif purchase == "city":
      if len(self.wheat) >= 2 and len(self.stone) >= 3:
        upgradeCity()
      else:
        print("Sorry! Not enough resources")

    elif purchase == "card":
      if len(self.wheat) >= 1 and len(self.sheep) >= 1 and len(self.stone) >= 1:
        purchaseCard()
      else:
        print("Sorry! Not enough resources")
    pass

  def loseResource():
    pass

  def stealResource():
    pass

  # Purchases and Builds
  def layRoad(self):
    pass

  def buildSettlement(self):
    pass

  def upgradeCity(self): #2 wheat, 3 stone
    pass

  def purchaseCard(self):
    pass

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
