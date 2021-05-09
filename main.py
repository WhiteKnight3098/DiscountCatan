import random as rand
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np


###SETUP###
root = Tk()
root.geometry('800x800')
leaderboard = Text(root, width = 35, height = 15, wrap='none')
leaderboard.pack()


#player
Coffee_Made = 0
Level = 0
Money = 100.00
sales_price = 1.00

Baristas = 0 #improves user clicks
Employee_Cost = 10.00
Shops = 0 #controls autoclick production
Expansion_Cost = 200.00

Beans = 50
Bean_prices = []
Bean_Current = 0
Beans_rate = 200

###FUNCTIONS###

def update_leaderboard():
  bean_price_relay()
  leaderboard.delete("1.0", "end")
  leaderboard.insert("end", 
  '''
  Current Status!
  Coffee Made: {}
  Money: {}
  Sale Price: {}
  Beans: {}
  Bean Price: {}
  Baristas: {}
  Employee_Cost: {}
  Shops: {}
  Expansion Cost: {}
  '''.format(Coffee_Made,Money,sales_price,Beans,Bean_Current,Baristas, Employee_Cost, Shops, Expansion_Cost))

def makeCoffee():
  global Coffee_Made
  global Beans
  global Money

  if Baristas >= 1:
    if Beans >= 1:
      Coffee_Made += 1
      Beans -= 1
      Money += sales_price
    else:
      print("Out of beans!")
    for b in range(Baristas):
      if Beans >= 1:
        Coffee_Made += 1
        Beans -= 1
        Money += sales_price
      else:
        ("You ran out of beans!")
  elif Beans >= 1:
    Coffee_Made += 1
    Beans -= 1
    Money += sales_price
  else:
    print("No beans available for use.")
  print(Coffee_Made)
  update_leaderboard()

#Put this here because bad organization. Worse than my cable management lmao    
btn = Button(root, text = "Make Coffee", bd = 5, command = makeCoffee)
btn.pack(side = 'top')


def buyBeans():
  global Money
  global Beans

  index = len(Bean_prices) - 1
  cost = Bean_prices[index]
  if Money >= cost:
    Money = Money - cost
    Beans += Beans_rate
  else:
    print("Lacking sufficient funds to purchase beans.")
  update_leaderboard()


def bean_price_relay():
  global Bean_Current
  list_length =  len(Bean_prices)
  if list_length > 14:
    Bean_prices.pop(0)
  price = rand.randint(20,50)
  Bean_prices.append(price)
  index = len(Bean_prices) - 1
  Bean_Current = Bean_prices[index]


def hire_barista():
  global Money
  global Baristas
  global Employee_Cost

  if Money >= Employee_Cost:
    Money -= Employee_Cost
    Baristas += 1
    Employee_Cost = Employee_Cost + (Employee_Cost/2)
  else:
    print("Lacking sufficient funds to hire staff.")
  update_leaderboard()

#TODO: Make Sale price button for raising and lowering coffee cost
def sales_price_up():
  global sales_price
  sales_price += 0.05
def sales_price_down():
  global sales_price
  sales_price -= 0.05

#TODO: make the purchase for an Autoclicker.
def purchase_shop():
  pass

#TODO: make matplotlib chart of current and past bean prices.
def bean_plot():
  pass


#TODO: Eventually I think the while loop needs to become a TKinter mainloop. Thus allowing the .after() method for the autoclicker functions.
#       for testing, this is just jerry-rigged thing to get us working.
root.mainloop()