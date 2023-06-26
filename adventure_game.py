import time
import random
import sys
import shutil

score = 0

def enter_game():
    print_pause("Would You Like to Try My Game? ".center(get_terminal_width()))
    choice = make_choice("", ["y", "n"])
    if choice == "y":
        the_game()
    elif choice == "n":
        print_pause("Okay")
        sys.exit()
    else:
        print_pause("Please Enter Yes or No".center(get_terminal_width()))

def get_terminal_width():
    # Get the width of the terminal
    terminal_width, _ = shutil.get_terminal_size(fallback=(80, 24))
    return terminal_width

def print_pause(message, seconds=1):
    # Print a message and wait for seconds.
    message_lines = message.split("\n")
    for line in message_lines:
        if line.strip() == "":
            delay_time = 0.0000000000000000000000000000000000000000000000000000000000000000000004  # Adjust the delay time for empty lines as needed
        else:
            delay_time = 0.00000000000000000000000000000000000000000000000000000000000000000000002  # Adjust the initial delay time for lines with text

        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            if not char.isspace():
                time.sleep(delay_time)  # Initial fast speed until reaching the text
                delay_time = 0.04  # Regular delay time after reaching the text
            else:
                time.sleep(0.000000000000000000000000000000000000000000000000000000000000000000000000000002)  # Additional delay for whitespace characters
        time.sleep(seconds)
        print()

def make_choice(decision, options):
    # Make the player make a decision and tell them if it's incorrect.
    terminal_width = get_terminal_width()
    decision_centered = decision.center(terminal_width)
    for char in decision_centered:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()  # Print a newline before displaying the options
    options_string = " / ".join(options)  # Concatenate options with a separator
    options_centered = options_string.center(terminal_width)
    print_pause(options_centered)  # Display options in the middle of the screen
    choice = ""
    while choice not in options:
        choice = input()
        print_pause(choice)
        if choice not in options:
            print_pause("Please choose one of the given choices".center(terminal_width))
    return choice


def new_score(point):
    # Show the score for the player
    global score
    score += point

def score_check():
    # Check if the player has won or lost
    if score >= 50:
        print_pause("Congratulations! You WIN".center(get_terminal_width()))
        print_pause(("Your Score is " + str(score)).center(get_terminal_width()))
    else:
        print_pause("Unfortunately, You have lost".center(get_terminal_width()))
        print_pause(("Your Score is " + str(score)).center(get_terminal_width()))

def replay_game():
    # Ask the player if they want to replay the game.
    choice = make_choice("Would you like to replay the game?", ["y", "n"])
    if choice == "y":
        global score
        score = 0
        the_game()
    else:
        print_pause("Thank you for playing the game.")

def intro():
    # Make the player know what is happening
    print_pause("You find yourself standing in an open field".center(get_terminal_width()))
    print_pause("filled with grass and yellow wildflowers.".center(get_terminal_width()))
    print_pause("Rumor has it that a wicked fairy is somewhere around here".center(get_terminal_width()))
    print_pause(("the weather was " + random.choice(weather)).center(get_terminal_width()))
    print_pause(("In front of you is a house that is colorful " + random.choice(color)).center(get_terminal_width()))
    print_pause("To your right is a dark cave.".center(get_terminal_width()))
    print()  # Print a newline after the intro

def knocking_on_the_door():
    # Make the player make a decision to knock on the door or not
    print_pause("Door opens, woman with a barking big dog appears.".center(get_terminal_width()))
    print_pause("Enter 1 to talk to the woman".center(get_terminal_width()))
    print_pause("Enter 2 to run away".center(get_terminal_width()))
    choice = make_choice("", ["1", "2"])
    if choice == "1":
        print_pause("Woman asks, Who are you?".center(get_terminal_width()))
        print_pause("You explain getting I'm lost from my friends.".center(get_terminal_width()))
        print_pause("You clarify being lost after hanging out with friends.".center(get_terminal_width()))
        print_pause("Woman reveals Alaska as your location!".center(get_terminal_width()))
        print_pause("Shocked, you have a fatal heart attack.".center(get_terminal_width()))
        new_score(10)
        score_check()
        replay_game()
    else:
        print_pause("You run away".center(get_terminal_width()))
        new_score(5)
        print_pause("Game Over".center(get_terminal_width()))
        score_check()
        replay_game()

def the_cave():
    # Make the player take a decision to walk in the cave or not
    print_pause("You enter the cave and see two paths: left and right.".center(get_terminal_width()))
    print_pause("1 Go to the Left".center(get_terminal_width()))
    print_pause("2 Go to the Right".center(get_terminal_width()))
    choice = make_choice("", ["1", "2"])
    if choice == "1":
        print_pause("You walk left.".center(get_terminal_width()))
        print_pause("You see a big bear that wants to attack you.".center(get_terminal_width()))
        print_pause("You attack the bear.".center(get_terminal_width()))
        print_pause("You kill the bear.".center(get_terminal_width()))
        print_pause("After killing the bear, you find your friends and go with them.".center(get_terminal_width()))
        new_score(60)
        score_check()
        replay_game()
    elif choice == "2":
        print_pause("You try to run away, but the bear catches you.".center(get_terminal_width()))
        print_pause("Game Over".center(get_terminal_width()))
        new_score(20)
        score_check()
        replay_game()

def the_game():
    # Start the game.
    intro()
    print_pause("1 Go to the house".center(get_terminal_width()))
    print_pause("2 Go to the cave".center(get_terminal_width()))
    choice = make_choice("", ["1", "2"])  # Empty string for the decision prompt
    if choice == "1":
        knocking_on_the_door()
        new_score(10)
    elif choice == "2":
        the_cave()
        new_score(10)

color = ['blue', 'red', 'white', 'black', 'orange', 'purple', 'green']
house_color = random.choice(color)
weather = ['Rainy', 'Snowy', 'Windy', 'Sunny', 'Clear']

print_pause("Welcome to the Game!".center(get_terminal_width()))
enter_game()
