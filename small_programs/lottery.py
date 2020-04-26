# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:55:00 2019

@author: GINNI
"""
#
#user can pick 6 numbers.
#Lottery calculates 6 random numbers
#Then we match the user numbers to the lottery numbers
#and calculate the winnings based on the numbers matched.
import random

def menu():
    user_data=get_player_numbers()
    lottery_data=lottery_numbers()
    results=user_data.intersection(lottery_data)
    print("You matched {}.You have won ${}".format(results,100**len(results)))
 
def get_player_numbers():
    user_numbers=input("Enter your six numbers, seprtaed by commas:")
    modiefied_number=user_numbers.split(",")
    updated_list=[int(num) for num in modiefied_number]
    return updated_list
    
#print(get_player_numbers())

def lottery_numbers():
    values=set()
    while len(values)<6:
        values.add(random.randint(1,20))
    return values

#print(lottery_numbers())
menu()



    