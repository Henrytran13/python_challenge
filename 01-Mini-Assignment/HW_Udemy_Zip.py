#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 11:22:12 2020

@author: henrytran
"""

import os
import csv

udemy_csv = os.path.join("/Users/henrytran/gwu-arl-data-pt-09-2020-u-c/02-Homework/03-Python/01-Mini-Assignment/2.11-HW_UdemyZip/Resources/web_starter.csv")


title =[]
price =[]
subscribers =[]
review = []
review_percent= []
length = []

with open(udemy_csv, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        
        course_title = row[1]
        title.append(course_title)
        
        course_price = row[4]
        price.append(course_price)
        
        course_subscribers = row[5]
        subscribers.append(course_subscribers)
        
        course_review = row[6]
        review.append(course_review)
        
        percent = round(float(course_review) / float(course_subscribers))
        review_percent.append(percent)
        
        new_length = row[9].split(" ")
        length.append(float(new_length[0]))
        
cleaned_csv = zip(title, price, subscribers, review, review_percent, length)

        
output_file =os.path.join("Udemy_web_final.csv")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left", 
                     "Percent of Review", "Length of Course"])
    writer.writerows(cleaned_csv)
    






