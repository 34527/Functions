import random

def specify_counter():
    counter_number = int(input("Please enter a number between 10 and 50: "))
    if counter_number <=50 and counter_number >=10:
        return counter_number
    else:
        print("Invalid input")

def counter_calculation(counter_number):
    while counter_number > 0:
        player_remove = int(input("How many counters do you want to take off: "))
        if player_remove <=3 and player_remove > 0:
            counter_number = counter_number - player_remove
            
            if counter_number > 0:
                computer_remove = random.randint(1,3)
                counter_number = counter_number - computer_remove
                
                if counter_number <=0:
                    victory = True
                    return victory
            else:
                victory = False
                return victory
        else:
            print("invalid input")

def output(victory):
    if victory is True:
        print("Player wins!")
    else:
        print("Computer wins!")
        
            



def counter_game():
    counter_number = specify_counter()
    victory = counter_calculation(counter_number)
    output(victory)

counter_game()
    
