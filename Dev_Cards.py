import random as rand

# Individual Card Controls
class Card():
  def __init__(self, name, ability):
    self.name = name
    self.ability = ability

  # Play Methods
  def showCard(self):
    print(self.name)

  # Debug methods


# Main deck for holding Dev Cards and deck functions
class Deck():

  Deck = []

  def __init__(self):
    self.build_deck()

  # Play Methods
  def build_deck(self):
    for knight in range(14):
      Deck.append(Card("knight"))
    for victory in ["Chapel", "University", "Market", "Palace", "Library"]:
      Deck.append(Card(victory))
    for i in range(2):
      for support in ["Monopoly", "Year of Plenty", "Road Building"]:
        Deck.append(Card(support))

  def shuffle(self):
    self.shuffle = rand.shuffle(Deck)

  def drawCard(self):
    self.drawCard = Deck.pop()
    return self.drawCard
  
  # Debug Methods
  def showDeck(self):
    for card in range(Deck):
      Card.showCard()
