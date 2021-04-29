import random as rand

def DiceRoll():
  alpha = rand.randint(1,6)
  beta = rand.randint(1,6)
  fina = alpha + beta
  return fina


# Desert tile is not included, neither are 7s which trigger the Bandit
def TokenLogger():
  randomized_tokens = []
  values_list = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
  for i in values_list:
    current = 19 - i
    number = rand.randint(0,current)
    randomized_tokens.append(number)
  return randomized_tokens

def Tilelogger()