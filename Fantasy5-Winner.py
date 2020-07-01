0# -*- coding: utf-8 -*-
"""
Created on Wed June 08:33:07 2019

@author: 
"""

# a Lotto simulator ...
# here we let the user pick the last winning numbers and the computer runs the tickets for a match
#
# the user selects 5 unique random numbers from 1 to 42 and creates a list
# the computer generates similar lists and compares these lists with the user list
# whenever there are 3, 4, 5 or 6 matches, corresponding counters are updated
# finally all the matches are shown
# tested with Python3.7        Spyder Winpython3.7
import random

def computer_random():
    """let the computer create a list of 5 unique random integers from 1 to 42"""
    ci = random.sample(range(1,43),5)
    return ci

   
def user_picks():
    """let the user create a list of 6 unique random integers from 1 to 42"""
    print ("Enter the second to last posted Fantasy 5 lotto numbers from 1 to 42:")
    ui = []
    while len(ui) < 5:
        print (len(ui) + 1,)
        try:
            i = int(input("--> "  ))
            # check if i is unique and has a value from 1 to 42
            # and is an integer, otherwise don't append
            if (i not in ui) and (1 <= i <= 42): 
                ui.append(i)
        except:
            print ("Enter an integer number!")
    return ui

def numcheck(list1, list2):
    """to find the number of matching items in each list use sets"""
    set1 = set(list1)
    set2 = set(list2)
    #set3 contains all items common to set1 and set2
    set3 = set1.intersection(set2)
    # return number of matching items
    return len(set3)
   
user_list = sorted(user_picks())
user_list1 = sorted(user_picks())
## '[05,17,24,27,41]' hit twice
print ("The Last two sets of Fantasy 5 Winning numbers were:", user_list,"and next", user_list1)
# set up counters for 3 to 5 matches
match3 = 0
match4 = 0 
match5 = 0
comp_list = sorted(computer_random())

# the computer picks the numbers for each ticket odds 1 in 850668 thousand
ticket_odds = 50000000
print ("Just a moment ...")
for k in range(ticket_odds):
    comp_list = sorted(computer_random())
    comp_list1 = sorted(computer_random())
    matches = numcheck(comp_list, user_list)
    matches1 = numcheck(comp_list1, user_list1)
    if matches == 3 and matches1 ==3 :
        match3 += 1
        #print("matched 3",comp_list,comp_list1)
        
        
    elif matches == 4 and matches1 ==4:
        match4 += 1
        print ("The 4 out of 5 Winning numbers from:",comp_list,"or",comp_list1)
        comp_list = sorted(computer_random())
        comp_list1 = sorted(computer_random())
        print ("The Winning numbers are:",comp_list,"or",comp_list1) #print the next generated number
        break
    elif matches == 5 and matches1 ==5:
        match5 += 1
        print( "The Last Winning numbers were:",comp_list)
        comp_list = sorted(computer_random())
        comp_list1 = sorted(computer_random())
        print ("The Next Winning numbers are:",comp_list,"or",comp_list1) #print the next generated number
        break
    # optional progress indicator
    if k % 10000000 == 0:
        print;print (">",k,"iterations so far")
    
#print; print
print ("Out of %d to 1 odds the computer found these matches:" % ticket_odds)
print ("3 matches = %d" % match3)
print ("4 matches = %d" % match4)
print ("5 matches = %d" % match5)
if match5==0:
    
    print("Try running again?")


