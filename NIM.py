#* ***********************************************************************
# Hassan Ali
# Assignment 4: NIM
# Computer Science 20 Block 3
# April 1, 2021

# This program is my own work - H.A.

import random

#The total number of stones at the start of the program
totalnumstones = random.randint(15, 30)


#This is a function that takes in user input and checks whether it is valid or not
def ValidEntry(totalnumstones):
    if totalnumstones > 1: #This is the path that the program will usually take
        stonestakenbyuser = input(f"There are {totalnumstones} stones. How many would you like? ")
    if totalnumstones == 1: #this is the path that the program will take when there is just one stone in order to ensure proper grammatical practice
        stonestakenbyuser = input(f"There is {totalnumstones} stone. How many would you like? ")
    while stonestakenbyuser.isnumeric() == False: #This is the path taken by the program when something other than a positve integer is entered
        stonestakenbyuser = input("Please enter a number (1, 2, or 3) ")
    stonestakenbyuser = int(stonestakenbyuser)
    while stonestakenbyuser > 3: #This is the path taken by the program when the player enters a number that is too high
        stonestakenbyuser = input("Please enter a number (1, 2, or 3) ")
        while stonestakenbyuser.isnumeric() == False: #This is the path taken by the program when something other than a positve integer is entered
            stonestakenbyuser = input("Please enter a number (1, 2, or 3) ")
        stonestakenbyuser = int(stonestakenbyuser)
    while stonestakenbyuser > totalnumstones: #This is the path entered by the program when there are not as many stones left as the user wants to take
        stonestakenbyuser = input("There are not that many stones left. Please enter a valid number: ")
        stonestakenbyuser = int(stonestakenbyuser)
        while stonestakenbyuser > 3: #This is the path taken by the program when the player enters a number that is too high
            stonestakenbyuser = input("Please enter a number (1, 2, or 3) ")
            while stonestakenbyuser.isnumeric() == False: #This is the path taken by the program when something other than a positve integer is entered
                stonestakenbyuser = input("Please enter a number (1, 2, or 3) ")
            stonestakenbyuser = int(stonestakenbyuser)
    totalnumstones -= stonestakenbyuser #Adjusting the total number of stones to a new value based on how many stones were taken by the user
    if totalnumstones == 0: #What happens when the player takes the last stone
        print("The computer beats the player!")
    return totalnumstones #The value that is returned by the function


#This is a function that has the computer take a certain number of stones
def drawStones(totalnumstones):
    stonescomp = 0 #making a variable and making it equal to 0 at first
    if totalnumstones >= 3: #This is the path taken when there are more than or equal to three total stones
        stonescomp = random.randint(1, 3)
        print(f"There are {totalnumstones} stones. The computer takes {stonescomp} stones.")
        if totalnumstones == 3 and stonescomp == 3: #this is what happens if the computer takes the last 3 stones all at once (the player beats the computer)
            print("The player beats the computer!")
    if totalnumstones == 2: #This is what happens when there are two stones left
        stonescomp = random.randint(1, 2)
        print(f"There are {totalnumstones} stones. The computer takes {stonescomp} stones.")
        if stonescomp == 2: #If the computer takes both of the two stones the player beats the computer
            print("The player beats the computer!")
    if totalnumstones == 1: #this is what happens when there is one stone left for the computer to take(the player beats the computer)
        stonescomp = 1
        print(f"There is {totalnumstones} stone. The computer takes {stonescomp} stone.")
        print("The player beats the computer!")
    totalnumstones -= stonescomp #adjusting the total number of stones based on the number of stones taken by the computer
    return totalnumstones #the value that is returned by the function


#This is a while loop that runs the two functions until the total number of stones is not 0
while totalnumstones != 0:
    totalnumstones = ValidEntry(totalnumstones)
    totalnumstones = drawStones(totalnumstones)
