#!/usr/sbin/env python3

"""
OPS435 Assignment 1 - Fall 2019
Program: a1_[student_id].py (replace student_id with your Seneca User name)
Author: "Student Name"
The python code in this file (a1_[Student_id].py) is original work written by
"Student Name". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
"""

import os,sys


def dbda(date, days):
    #print('{},{}'.format(date,days))
    if days > 0:
        after(date,days)
        print('positive')
        print(after(date,days))

    elif days == 0:
        pass
    #elif kwargs != 0:
    #    for i in kwargs:
    #        return(i * after(date,i))

    else:
        before(date,days)
        print('negative')
        print(before(date,days))

def leap_year(year):
    
    lyear = year % 4 

    if lyear == 0:
        feb_max = 29

    else:
        feb_max = 28

    lyear = year % 100 

    if lyear == 0:
        feb_max = 28

        lyear - year % 400  

    if lyear == 0:
        feb_max = 29 

    return feb_max


def after(date,days):   
    #print('testing after def')
    if len(date) != 10:
        #return '0000/00/00'
        print('Error: wrong date entered')
        sys.exit()

    else:
        str_year, str_month, str_day = date.split('/')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)
        #print(year,month,day)
        if month > 12:
            print("Error: wrong month entered") 
            sys.exit()

        elif day > 31:
            print("Error: wrong day entered")
            sys.exit()

        lyear = year % 4 

        if lyear == 0:
            feb_max = 29

        else:
            feb_max = 28

        lyear = year % 100 

        if lyear == 0:
            feb_max = 28

            lyear - year % 400  

        if lyear == 0:
            feb_max = 29 
        
        tmp_day = day + days

        mon_max = {1:31, 2:feb_max, 3:31, 4:30, 5:31, \
            6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        
        #if days + mon_max[month] > mon_max[month]:
        #    tmp_month = month + round(days / mon_max[month])
        #    to_day = (day + mon_max[month]) % mon_max[month]
        if tmp_day > mon_max[month]:
            to_day = tmp_day % mon_max[month]
            tmp_month = month + (-(-tmp_day // mon_max[month])) - 1
            #to_day = tmp_day % mon_max[tmp_month]
            
        else:
            to_day = tmp_day
            tmp_month = month + 0 

        #if day <= days

        if tmp_month > 12:
            to_month = tmp_month % 12
            #to_day = (- to_month)+ round(tmp_day / mon_max[month])
            year = year + tmp_month / 12
            year = int(year)
            new_year = leap_year(year)
            print(new_year)
            mon_max = {1:31, 2:new_year, 3:31, 4:30, 5:31, \
            6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
            to_day = round(tmp_day / mon_max[to_month])

        #if days > year:
        #    year = year + round((- days) / 365)
        else:
            to_month = tmp_month + 0
        
        next_date = str(year)+"/"+str(to_month).zfill(2)+"/"+str(to_day).zfill(2)

        return next_date


def before(date,days):
    print('Testing')
        #print('testing after def')
    if len(date) != 10:
        #return '0000/00/00'
        print('Error: wrong date entered')
        sys.exit()

    else:
        str_year, str_month, str_day = date.split('/')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)
        #print(year,month,day)
        if month > 12:
            print("Error: wrong month entered") 
            sys.exit()

        elif day > 31:
            print("Error: wrong day entered")
            sys.exit()

        lyear = year % 4 

        if lyear == 0:
            feb_max = 29

        else:
            feb_max = 28

        lyear = year % 100 

        if lyear == 0:
            feb_max = 28

            lyear - year % 400  

        if lyear == 0:
            feb_max = 29 
        
        tmp_day = day + days 
        tmp_days = (- tmp_day)

        mon_max = {1:31, 2:feb_max, 3:31, 4:30, 5:31, \
        6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        
        #tmp_day = month[max] + negative

        if (- days) > day:
            #tmp_month = month - 1
            #if tmp_month < 1:
            #    tmp_month = 12 - tmp_month
            #else:    
            tmp_month = month - (-(-tmp_days // mon_max[month]))
            #to_day = day - round(tmp_days / mon_max[month])
            to_day = mon_max[tmp_month] - tmp_days % mon_max[month]
        
        elif (- days) == 1:
            tmp_month = month - 1
            if month == 1:
                tmp_month = 12
                year = year - 1
            to_day = mon_max[tmp_month] - tmp_days % mon_max[month]


        else:
            to_day = tmp_day
            tmp_month = month + 0

        #if (- days) > lyear: 
        #    year = year - round((- days) / 365)
        #    to_month = (- days) - month

        #if day == tmp_days:
        #    to_day = mon_max[tmp_month]
        #    print('testing11')

        if tmp_month < 1:
            to_month = (- tmp_month) % 12
            to_day = mon_max[to_month] - tmp_days % mon_max[month]
            year = year - tmp_month / 12
            year = int(year)

        else:
            to_month = tmp_month + 0
            tmp_month = month + 0
        
        next_date = str(year)+"/"+str(to_month).zfill(2)+"/"+str(to_day).zfill(2)

        return next_date

if __name__ == "__main__":

    try:
        if len(sys.argv) > 1 and sys.argv[1] != '--step': 
            date = sys.argv[1]
            days = int(sys.argv[2])
            dbda(date,days)

        elif sys.argv[1] == '--step':
            date = sys.argv[2]
            days = int(sys.argv[3])
            #steps = sys.argv[3]
            #steps = str(days)

            for i in range(1,days + 1):
                #print(i)
                dbda(date,i)
    
    except IndexError:
        print("Usage: ssha2.py [--step] YYYY/MM/DD +/-n")


