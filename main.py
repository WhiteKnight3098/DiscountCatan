#Credits:
#Tristan Stapert did a vast majority of the backend stuff, while Ben Gress focused on GUI and print outs within the window.

import random as rand
from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation

### SETUP ###

## Major Window components (Not yet including the graph) ##
# Root holds the TKinter widgets
root = Tk()
root.geometry('800x400')

#Current Statistics Text Box Widget
leaderboard = Text(root, width = 35, height = 15, wrap='none')
leaderboard.grid(column=1, columnspan=1, row=1, rowspan= 5)

#Game Updates Widget
newsfeed = Text(root, width = 100, height = 5, wrap='none')
newsfeed.grid(column=1, columnspan=20, row=6, rowspan= 1)

## Player Stats ##
# Generic Player Stats. Will be updated as game is played.
Coffee_Made = 0
Level = 0
Money = 100.00
sales_price = 3.00

Baristas = 0 #improves user clicks
Employee_Cost = 10.00

Shops = 0 #controls autoclick production
Expansion_Cost = 200.00

## Bean Controls ##
#starting supply
Beans = 50

# current and past minute prices for the graph
Bean_prices = []
Bean_Current = 0

# Purchase rate
Beans_rate = 200



### FUNCTIONS ###

# Update the current game statistics
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

# Inputs the news feed for the failed purchases
def insufficientFunds():
  newsfeed.insert("1.0", "Lack of sufficient funds!\n")

# Inputs the news feed for the failed coffee production
def noBeans():
  newsfeed.insert("1.0", "No more beans!\n")

# Main function of the game. Makes a coffee and adds income to the current Money
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
      noBeans()
    for b in range(Baristas):
      if Beans >= 1:
        Coffee_Made += 1
        Beans -= 1
        Money += sales_price
      else:
        noBeans()
  elif Beans >= 1:
    Coffee_Made += 1
    Beans -= 1
    Money += sales_price
  else:
    noBeans()
  update_leaderboard()

# Button layout for the buttons of the game
Coffeebtn = Button(root, text = "Make Coffee", bd = 2, command = makeCoffee)
Coffeebtn.grid(column=2, row=1)


# Adds more beans to the current stock
def buyBeans():
  global Money
  global Beans

  index = len(Bean_prices) - 1
  cost = Bean_prices[index]
  if Money >= cost:
    Money = Money - cost
    Beans += Beans_rate
    newsfeed.insert('1.0', 'Beans acquired\n')
  else:
    insufficientFunds()
  update_leaderboard()

Beansbtn = Button(root, text = "Buy Beans", bd = 2, command= buyBeans)
Beansbtn.grid(column=2,row=2)


# Improve output rate of manual production
def hire_barista():
  global Money
  global Baristas
  global Employee_Cost

  if Money >= Employee_Cost:
    Money -= Employee_Cost
    Baristas += 1
    Employee_Cost +=(Employee_Cost/2)
    newsfeed.insert('1.0', 'Barista Hired\n')
  else:
    insufficientFunds()
  update_leaderboard()

BaristaButton = Button(root, text = "Hire Barista", bd = 2, command = hire_barista)
BaristaButton.grid(column=2, row=3)


# Purchase a shop expansion to start generating income
def purchase_shop():
  global Money
  global Shops
  global Expansion_Cost
  
  if Money >= Expansion_Cost:
    Money -= Expansion_Cost
    Shops += 1
    Expansion_Cost += (Expansion_Cost/2)
    newsfeed.insert('1.0', 'Shop expanded. Autogeneration begun\n')
  else:
    insufficientFunds()
  update_leaderboard()

ShopButton = Button(root, text = "Expand Shop", bd = 2, command= purchase_shop)
ShopButton.grid(column=2, row=4)


#Auto clicker function for Shop Expansion
def shop_generator():
  global Money
  global Coffee_Made
  global Beans

  for shop in range(Shops):
    if Beans >= 1:
      makeCoffee()
    else:
      noBeans()
  root.after(1000, shop_generator)


# Graph control for the Bean Sale Prices for the last minute
def bean_plot(i):
  xtime = []
  if len(Bean_prices) < 16:
    for x in range(len(Bean_prices)):
      xtime.append(x)
  plt.xlabel("Time")
  plt.ylabel("Price of Beans")
  plt.title("Bean Stock Prices")
  chart.clear()
  chart.plot(xtime, Bean_prices)


#Function that automatically generates the next bean prices that will be used.
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


### Initiation ###

#Start timed automation
shop_generator()

#Generate first price
bean_price_relay()

#Begin Graph of stocks
fig = plt.figure()
chart = fig.add_subplot(111)
bean_graph = animation.FuncAnimation(fig, bean_plot, interval=1000)
plt.tight_layout()
plt.show()

#Window Keep-alive
root.mainloop()