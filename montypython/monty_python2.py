#!/usr/bin/env python3
"""Work with if, elif, else & while"""


round = 0
answer= ""

while round < 3 and answer.lower() != "brian": 
    round = round + 1
    print("Finish the movie title, 'Monty Python\'s The Life of _____'")
    answer = input("Your guess--> ")

    if answer.lower() == 'Brian':
        print("Correct")
        #break
    elif round==3: 
        print("Sorry, the was Brian.")
        #break
    else:
        print("Sorry, try again!")
    
