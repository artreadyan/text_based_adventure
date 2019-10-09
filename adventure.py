import time
print("Simple Text Based Adventure Game")
time.sleep(2)

def enter_name():
    adventurer_name = input("Welcome to a simple maze. Adventurer, what is your name? ")

    if adventurer_name:
        print("\nWelcome " + adventurer_name.upper() + "! You are now in a room with 3 articles. Choose 1 that will lead you to your fate.\n")
    else:
        enter_name()

def start_room():
    enter_name()
    choices_room()

def room_four():
    choice = input("Congratulations! You have finished the game! Do you want to play again? (y/n)")
    if choice == "y":
        time.sleep(1)
        start_room()
    else:
        exit()

def choices_room():
    room_choice = input("\nThis is the choice room. here are 3 choices: AXE, BOOK and ARROW. Please choose 1: ")
    time.sleep(1)

    if room_choice.lower() == "axe":
        password = input("\nYou are now in the room of the Vikings! Solve the riddle and you shall have a price. Get it wrong, misfortune will fall on you.\n What is the password?(Clue: Bungo Stray Dogs): \n")

        if password.lower() == "dazai osamu":
            room_four() 
        else: 
            print("Okay. You're dead. Bye.")
            start_room()
        

    elif room_choice.lower() == "book":
        print("You have reached the room for books. Enjoy your stay for 5 seconds")
        time.sleep(5)
        choices_room()
    
    elif room_choice.lower() == "arrow":
        print("There are 2 doors numbered as 1 & 2. Choose wisely.")
        door = int(input("Enter the door you wished to open: "))

        if door == 1:
            room_four()
        
        elif door == 2:
            print("Okay, teleporting you to the start room 5 seconds...")
            time.sleep(5)
            choices_room()

start_room()


