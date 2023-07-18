#IMPORTED LIBRARIES
import random
import time

#FUNCTIONS
def RPS():
    rps_options = ["Rock", "Paper", "Scissors", "rock", "paper", "scissors", "r", "R", "p", "P", "s", "S"]
    time.sleep(0.4)
    user_input_rps = input("\n>> Select 'Rock', 'Paper', or 'Scissors': ")

    while user_input_rps not in rps_options:
        time.sleep(0.4)
        user_input_rps = input(">> Invalid Input!: ")
        time.sleep(0.4)

    selected_dictionary = {"r": "Rock", "R": "Rock", "p": "Paper", "P": "Paper", "s": "Scissors", "S": "Scissors"}

    try:
        user_selected = selected_dictionary[user_input_rps].upper()
    except KeyError:
        user_selected = user_input_rps.upper()

    time.sleep(0.4)
    print("\n>> Letting the Opponent Select!")
    time.sleep(1)
    print(">> Please Wait...")
    computer_selected = random.choice(rps_options[0:3]).upper()
    time.sleep(2)
    print("\n>> Your Opponent has made a Choice!")
    time.sleep(2.5)
    print("\n>> Lets Give it a Countdown!")
    time.sleep(1)
    print(" - Rock!")
    time.sleep(1)
    print(" - Papers!")
    time.sleep(1)
    print(" - Scissors!")
    time.sleep(1)
    print("\n>> SHOW TIME! LETS SEE WHO WON!")
    time.sleep(1.5)
    print("\n>> You Chose: " + user_selected)
    time.sleep(1)
    print(">> Your Opponent Chose: " + computer_selected)
    print("")
    time.sleep(1)

    if user_selected == computer_selected:
        time.sleep(0.6)
        print(">> ITS A DRAW!")
        return None
    elif ((user_selected == "ROCK") and (computer_selected == "PAPER")) or ((user_selected == "PAPER") and (computer_selected == "SCISSORS")) or ((user_selected == "SCISSORS") and (computer_selected == "ROCK")):
        print(">> YOU LOST! Better Luck Next Time!")
        return False
    else:
        print(">> CONGRATULATIONS! YOU WON!")
        return True

#MAINSCREEN
Yes = ["yes", "YES", "Yes", "yEs", "yeS", "YeS", "Y", "y", "yE", "ye", "YE", "Ye"]
No = ["No", "no", "NO", "nO", "N", "n"]

Valid = Yes + No
time.sleep(0.6)

print('''
   __    ___  ___                           
  /__\  /___\/ __\ /\ /\                    
 / \// //  // /   / //_/                    
/ _  \/ \_// /___/ __ \                     
\/ \_/\___/\____/\/  \/                                       
   ___  _      ___  __  __                  
  / _ \/_\    / _ \/__\/__\                 
 / /_)//_\\\  / /_)/_\ / \//                 
/ ___/  _  \/ ___//__/ _  \                 
\/   \_/ \_/\/   \__/\/ \_/                                              
 __    ___  _____  __  __    ___  __  __    
/ _\  / __\ \_   \/ _\/ _\  /___\/__\/ _\   
\ \  / /     / /\/\ \ \ \  //  // \//\ \    
_\ \/ /___/\/ /_  _\ \_\ \/ \_// _  \_\ \   
\__/\____/\____/  \__/\__/\___/\/ \_/\__/                                        
''')

time.sleep(0.3)
user_input = input("\n>> Start the Game? (Yes or No): ")

# VALIDATION CHECKS FOR STARTING OR NOT
while user_input not in Valid:
    time.sleep(0.3)
    user_input = input(">> Invalid Input! Enter 'Yes' or 'No': ")

Score_User = 0
Score_Computer = 0

while user_input in Yes:
    time.sleep(0.3)
    Is_Winner = RPS()
    time.sleep(1)

    if Is_Winner != None and (Is_Winner):
        Score_User += 1
    elif Is_Winner != None and (not Is_Winner):
        Score_Computer += 1

    print("\n>> Your Score: " + str(Score_User))
    print(">> Opponent's Score: " + str(Score_Computer))

    time.sleep(0.5)
    user_input = input("\n>> Start Again? (Yes or No): ")

    while user_input not in Valid:
        time.sleep(0.5)
        user_input = input(">> Invalid Input! Enter 'Yes' or 'No': ")

    if user_input in No:
        time.sleep(0.5)
        user_input = input("\n>> Confirm? (Yes or No): ")
        if user_input in Yes:
            break
        else:
            user_input = "Yes"

time.sleep(0.6)
print(''' 

   ____  __ _____  __________    __  ___   _____        __     ___   _              __ 
  /__\ \/ / \_   \/__   \_   \/\ \ \/ _ \ /__   \/\  /\/__\   / _ \ /_\    /\/\    /__\\
 /_\  \  /   / /\/  / /\// /\/  \/ / /_\/   / /\/ /_/ /_\    / /_\///_\\\  /    \  /_\  
//__  /  \/\/ /_   / //\/ /_/ /\  / /_\\\   / / / __  //__   / /_\\\/  _  \/ /\/\ \//__  
\__/ /_/\_\____/   \/ \____/\_\ \/\____/   \/  \/ /_/\__/   \____/\_/ \_/\/    \/\__/                                                                                     
''')

time.sleep(2)
