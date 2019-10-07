#!/usr/sbin/env python3
"""
OPS435 Assignment 1 - Fall 2019
Program: a1_ssha2.py
Author: "Sang Soo Ha"
The python code in this file (a1_ssha2.py) is original work written by
"Sang Soo Ha". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
"""

import os,sys


def usage():
    """
    This usage function is to check how many arguments were given, 
    and to give a guidance to users that the the number of arguments
    should be no more or less than 3 and 4. 
    """

    if len(sys.argv) !=3 or not 4:
        print(f"{sys.argv[0]} [--step] YYYYMMDD +/-n")
        sys.exit()


def valid_date(date):
    '''
    This function validates whether the year, month, or day was entered correctly,
    or the length of the date is sufficient or not. 
    '''
    if len(date) != 10:
        print("Error: wrong date entered")
        sys.exit()
    else:
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])
        if month > 12: 
            print("Error: wrong month entered")
            sys.exit()
        elif day >31:
            print('Error: wrong day entered')
            sys.exit()
        return date


def dbda(date, days):
    '''
    This function requires two parameters: date and entered days.
    If the days are greater than 0, it will invoke the tomorrow function
    If less than 0, it will invoke the yesterday function
    '''
    #print('{},{}'.format(date,days))
    if days > 0:
        for i in range(days):
            date = tomorrow(date)
            #print(date)
        #print('positive')
        #print(tomorrow(date,days))
        print(date)
    elif days == 0:
        pass

    else:
        #days = - days
        for i in range(-days):
            date = yesterday(date)
        #print('negative')
        #print(yesterday(date,days))
        print(date)
    return date


def leap_year(lyear):
    
    if (lyear % 4 == 0): 
        if (lyear % 100 == 0):
            if (lyear % 400 == 0):
                leapyear = True
            else: 
                leapyear = False
        else:
            leapyear = True   
    else: 
         leapyear = False   
    
    return leapyear


def days_in_mon(year):
    '''
    This function returns the maximum date of the month entered, including the result
    of the leap year
    '''
    if leap_year(year):
        feb_max = 29
    else:
        feb_max = 28

    mon_max = {1:31, 2:feb_max, 3:31, 4:30, 5:31, \
    6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    return mon_max


def tomorrow(date):   
    '''
    This function returns the next day of the date entered, using other functions
    to validate the date and to get the maximum days of the month.
    '''
    #print('testing after def')
    #if len(date) != 10:
    #    #return '0000/00/00'
    #    print('Error: wrong date entered')
    #    sys.exit()
    date = valid_date(date)
    str_year, str_month, str_day = date.split('/')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)
    mon_max = days_in_mon(year)
    

    tmp_day = day + 1 # next day

    if tmp_day > mon_max[month]:
        to_day = tmp_day % mon_max[month] # if tmp_day > this month's max, reset to 1
        tmp_month = month + 1
    else:
      to_day = tmp_day
      tmp_month = month + 0

    if tmp_month > 12:
       to_month = 1
       year = year + 1
    else:
       to_month = tmp_month + 0

    next_date = str(year)+"/"+str(to_month).zfill(2)+"/"+str(to_day).zfill(2)
     
    return next_date


def yesterday(date):
    '''
    This function returns the previous day of the date entered, using other functions 
    previously created to validate the date and to get the maxium date of the month.
    '''
    #print('Testing')
        #print('testing after def')
#    if len(date) != 10:
#        #return '0000/00/00'
#        print('Error: wrong date entered')
#        sys.exit()
    date = valid_date(date)
    str_year, str_month, str_day = date.split('/')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)
    #print(day)
    mon_max = days_in_mon(year)
        
    tmp_day = day - 1
    #tmp_days = (- tmp_day)
        
        #tmp_day = month[max] + negative

    if tmp_day == 0: 
        month = month - 1
        #tmp_month = month  
        #tmp_month = to_month
        if month == 0: 
            #tmp_month = 12
            year -= 1
            month = 12
            tmp_day = mon_max[month]
            
        else:
            tmp_day = mon_max[month]
        #tmp_month = month - 1
        #if tmp_month < 1:
        #    tmp_month = 12 - tmp_month
        #else:    
        #tmp_month = month - (-(-tmp_days // mon_max[month]))
        #to_day = day - round(tmp_days / mon_max[month])
        #to_day = mon_max[tmp_month] - tmp_days % mon_max[month]
    else:
        year -= 0
        #tmp_day = tmp_day
        month -= 0
        
    next_date = str(year)+"/"+str(month).zfill(2)+"/"+str(tmp_day).zfill(2)

    return next_date

if __name__ == "__main__":
    
    usage()
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
    


