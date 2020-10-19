#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 11:04:25 2020

@author: henrytran
"""

shop = "y"
shopbuy_index = []  
shop_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", "Buleberry", "Buko",
             "Burek", "tamale", "Steak"]
print("Welcome to the House of Pie. Here our deliouse pies")

while shop == "y"  :
    print("____________________________________________________________________________")
    print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, " +
          " (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
          " (9) Tamale, (10) Steak ")
    pie_pick = int(input("Please enter your selection: "))
    shopbuy_index.append(pie_pick)
    
    
    print("Great, We'll have that " + shop_list[(pie_pick) - 1] + " right out for you")
    shop = input("Would you like to make another purchase: (y)es or (n)o ? ")

print("________________________________________________________________________________")
print("You bought a total of  " + str(len(shopbuy_index)) )2
