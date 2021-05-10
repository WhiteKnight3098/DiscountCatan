import random as rand
from tkinter import *
from typing import Collection
from matplotlib import pyplot as plt
""" import numpy as np """


###SETUP###
root = Tk()
root.geometry('800x400')
leaderboard = Text(root, width = 35, height = 15, wrap='none')
leaderboard.grid(column=1, columnspan=1, row=1, rowspan= 5)
newsfeed = Text(root, width = 100, height = 5, wrap='none')
newsfeed.grid(column=1, columnspan=20, row=6, rowspan= 1)

#TODO: Move function print statements into text box newsfeed

#player
Coffee_Made = 0
Level = 0
Money = 100.00
sales_price = 3.00

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
  '''.format(Coffee_Made,Money,sales_price,Beans,Bean_Current,Baristas,Employee_Cost,Shops,Expansion_Cost))

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
  update_leaderboard()

#Put this here because bad organization. Worse than my cable management lmao    
Coffeebtn = Button(root, text = "Make Coffee", bd = 2, command = makeCoffee)
Coffeebtn.grid(column=2, row=1)


def buyBeans():
  global Money
  global Beans

  index = len(Bean_prices) - 1
  cost = Bean_prices[index]
  if Money >= cost:
    Money = Money - cost
    Beans += Beans_rate
    newsfeed.insert('1.0', 'Beans acquired')
  else:
    print("Lacking sufficient funds to purchase beans.")
  update_leaderboard()

Beansbtn = Button(root, text = "Buy Beans", bd = 2, command= buyBeans)
Beansbtn.grid(column=2,row=2)


#TODO: Make Button
def hire_barista():
  global Money
  global Baristas
  global Employee_Cost

  if Money >= Employee_Cost:
    Money -= Employee_Cost
    Baristas += 1
    Employee_Cost +=(Employee_Cost/2)
    newsfeed.insert('1.0', 'Barista Hired')
  else:
    print("Lacking sufficient funds to hire staff.")
  update_leaderboard()
BaristaButton = Button(root, text = "Hire Barista", bd = 2, command = hire_barista)
BaristaButton.grid(column=2, row=3)


#TODO: make the purchase for an Autoclicker.
#TODO: Make button on GUI
def purchase_shop():
  global Money
  global Shops
  global Expansion_Cost
  
  if Money >= Expansion_Cost:
    Money -= Expansion_Cost
    Shops += 1
    Expansion_Cost += (Expansion_Cost/2)
    newsfeed.insert('1.0', 'Shop expanded')
  else:
    print("Lacking sufficient funds to expand business")
  update_leaderboard()

ShopButton = Button(root, text = "Expand Shop", bd = 2, command= purchase_shop)
ShopButton.grid(column=2, row=4)

#Auto clicker thing
def shop_generator():
  global Money
  global Coffee_Made
  global Beans

  for shop in range(Shops):
    if Beans >= 1:
      makeCoffee()
    else:
      print("No more beans!")
  root.after(1000, shop_generator)


#TODO: make matplotlib chart of current and past bean prices.
def bean_plot():
  xtime = []
  if len(Bean_prices) < 15:
    for x in range(len(Bean_prices)):
      xtime.append(x)
  print(xtime,Bean_prices)
  plt.plot(xtime, Bean_prices)
  plt.xlabel("Time")
  plt.ylabel("Price of Beans")
  plt.title("Bean Stock Prices")
  plt.show()
  root.after(5000,bean_plot)


# NO BUTTON NEEDED
def bean_price_relay():
  global Bean_Current
  list_length =  len(Bean_prices)
  if list_length > 14:
    Bean_prices.pop(0)
  price = rand.randint(20,50)
  Bean_prices.append(price)
  index = len(Bean_prices) - 1
  Bean_Current = Bean_prices[index]
  update_leaderboard()
  root.after(5000, bean_price_relay)



#TODO: Eventually I think the while loop needs to become a TKinter mainloop. Thus allowing the .after() method for the autoclicker functions.
#       for testing, this is just jerry-rigged thing to get us working.

bean_price_relay()
bean_plot()
shop_generator()
root.mainloop()