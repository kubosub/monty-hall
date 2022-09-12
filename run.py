'''This is a simulation of the Monty Hall problem'''
import random

def interactive():
    '''The interactive mode - make a manual choice.'''
    correct_door = random.randint(1,3) # one of three doors contain the prize
    player_choice = input_valid_integer("Which door do you choose? (1-3) ", 1, 2, 3)
    host_choice = remove_doors(correct_door, player_choice)

    change_doors = input_valid_integer(f"The gameshow host opens door number { host_choice }, "
                                        "- there is no prize behind the door.\n"
                                        "Do you wish to (1) change doors, or (2) stick to "
                                        "your original choice? ", 1, 2)

    if change_doors == 1:
        final_choice = remove_doors(host_choice, player_choice)
    else:
        final_choice = player_choice

    if final_choice == correct_door:
        print(f"You win! The correct door was indeed number { correct_door }!")
    else:
        print(f"Sorry, you lose... The correct door was number { correct_door }.")

def automatic():
    '''The automatic mode - simulate a large number of runs.'''
    strategy = input_valid_integer("(1) Always change doors when asked\n"
                                   "(2) Always stick to original choice\n"
                                   "Which strategy to apply? ", 1, 2)
    number_of_tries = input_valid_integer("How many tries to run? ")

    win_count = 0

    for _ in range(number_of_tries):
        correct_door = random.randint(1,3)
        player_choice = 1
        host_choice = remove_doors(correct_door, player_choice)

        if strategy == 1:
            final_choice = remove_doors(host_choice, player_choice)
        else:
            final_choice = player_choice

        if final_choice == correct_door:
            win_count += 1

    print(f"You won { win_count } times of { number_of_tries } tries. "
           "That's { float(win_count)/float(number_of_tries)*100 }% wins!")

def remove_doors(door1, door2):
    '''Remove two doors, or if they are the same door,
    remove one door return one random remaining door.'''
    valid_doors = list(range(1,4))
    valid_doors.remove(door1)
    if door1 != door2:
        valid_doors.remove(door2)
    return random.choice(valid_doors)

def input_valid_integer(prompt, *argv):
    '''Validate input, return integer. If argv integer(s) passed,
    only validate if user input matches an argv'''
    while True:
        user_input = input(prompt)
        try:
            user_input = int(user_input)
            if user_input < 1:
                raise ValueError("Sorry, no numbers below zero")
            if (argv and user_input in argv) or not argv:
                return user_input
        except ValueError:
            print("Does not compute. Try again.")

def main():
    '''Main program'''
    mode = input_valid_integer("(1) Interactive\n"
                 "(2) Automatic\n"
                 "Choice: ", 1, 2)

    if mode == 1:
        interactive()
    else:
        automatic()

if __name__ == '__main__':
    main()
