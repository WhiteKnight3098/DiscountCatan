class Player():
  def __init__(self, name):
    self.name = name
    self.player_hand = []  #dev cards
    self.resources = []  #Resource only

  # Resource Collection and Trades
  def addResource(self, diceroll, random_values, tiles):

    indexValues = []

    for number in range(len(random_values)):
      if diceroll == random_values[number]:
        indexValues.append(number)
    
    self.resources.append(tiles[number])
      
    pass
  def returnstone(self):
    value = self.resources[0]
    return value
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
