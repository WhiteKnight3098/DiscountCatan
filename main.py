import random as rand
import time
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np


###SETUP###

#player
Coffee_Made = 0
Level = 0
Money = 100
sales_price = 1.00
Baristas = 0
Managers = 0

Beans = 0
Bean_price = []
Beans_rate = 200

###FUNCTIONS###

def makeCoffee():
  global Coffee_Made
  global Beans

  if Beans >= 1:
    Coffee_Made += 1
    Beans -= 1

def buyBeans():
  global Money
  global Beans

  index = len(Bean_price) - 1
  cost = Bean_price[index]
  if Money >= cost:
    Money = Money - cost
    Beans += Beans_rate

def bean_price_relay():
  price = rand.randint(20,50)
  Bean_price.append(price)
"""   current = len(Bean_price) - 1
  print("Bean price: ${}".format(Bean_price[current])) """

def bean_plot():
  pass

while True:
  bean_price_relay()

  print('''
  Current Status!
  Coffee Made: {}
  Money: {}
  Sale Price: {}
  Beans: {}
  Bean Price: {}
  '''.format(Coffee_Made,Money,sales_price,Beans,Bean_price))

  print("Would you like to make coffee or buy beans?")
  choice = int(input("1. Coffee\n2. Beans\n"))
  if choice == 1:
    makeCoffee()
  elif choice == 2:
    buyBeans()
  else:
    print("Sorry! No can do!")
  #So that the money doesn't run out
  Money = 100