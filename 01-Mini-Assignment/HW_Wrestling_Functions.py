#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 21:05:55 2020

@author: henrytran
"""

import os
import csv


wrestling_csv = os.path.join('/Users/henrytran/gwu-arl-data-pt-09-2020-u-c/02-Homework/03-Python/01-Mini-Assignment/3.08-HW_WrestlingWithFunctions/Resources/WWE-Data-2016.csv')


def print_percentages(wrestler_data):
    
    name = str(wrestler_data[0])
    wins = int(wrestler_data[1])
    losses = int(wrestler_data[2])
    draws = int(wrestler_data[3])


    total_matches = wins + losses + draws

    win_percent = (wins / total_matches) * 100
    loss_percent = (losses / total_matches) * 100    
    draw_percent = (draws / total_matches) * 100

    
    if loss_percent > 50:
        type_of_wrestler = "Jobber"
    else:
        type_of_wrestler = "Superstar"

    # Print out the wrestler's name and their percentage stats
    print(f"Stats for {name}")
    print(f"WIN PERCENT: {win_percent}")
    print(f"LOSS PERCENT: {loss_percent}")
    print(f"DRAW PERCENT: {draw_percent}")
    print(f"{name} is a {type_of_wrestler}")


with open(wrestling_csv, 'r') as csvfile:

    
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    
    name_check_enter = input("What wrestler do you want to look for? ")

    
    for row in csvreader:

        
        if name_check_entercheck == row[0]:
            print_percentages(row)