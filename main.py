import random as rand
from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation



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

def insufficientFunds():
  newsfeed.insert("1.0", "Lack of sufficient funds!\n")

def noBeans():
  newsfeed.insert("1.0", "No more beans!\n")

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
    newsfeed.insert('1.0', 'Beans acquired\n')
  else:
    insufficientFunds()
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
    newsfeed.insert('1.0', 'Barista Hired\n')
  else:
    insufficientFunds()
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
    newsfeed.insert('1.0', 'Shop expanded. Autogeneration begun\n')
  else:
    insufficientFunds()
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
      noBeans()
  root.after(1000, shop_generator)


#TODO: make matplotlib chart of current and past bean prices.
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