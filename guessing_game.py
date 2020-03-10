"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random


# Store every score from every game
scores = []

# Return a random number between 1 and 10
def generate_number():
    return random.randint(1, 10)

def get_highscore(attempts_list, counter):
    highscore = 0
    # Loop over the stored scores
    for attempt in attempts_list:
        # Check if the list is empty or not
        if len(attempts_list) < 1:
            return '**no highscore yet**'
        # If the score is less\equal to the counter save it as highscore
        elif attempt <= counter:
            highscore = attempt

    return highscore

def start_game():
    # Create a counter to store how many turns are required find the number
    guess_counter = 0
    # Great the User
    print('-' * 38 + '\n Welcome to the Number Guessing Game!\n' + '-' * 38 + '\n')
    print('Current HIGHSCORE: {}'.format(get_highscore(scores, guess_counter)))

    # Use generate_number to generate a number
    random_solution = generate_number()

    # Try block for potential user inerrupt
    try:

        while True:
            try:
                guess = input('Pick a number between 1 and 10: ')
                guess = int(guess)
                
                guess_counter += 1
                
                if guess < 1 or guess > 10:
                    print('{} is out of range [1-10]. Try again...'.format(guess))
                    continue
                elif guess < random_solution:
                    print('It is higher!')
                    continue
                elif guess > random_solution:
                    print('It is lower!')
                    continue
                else:
                    print('\nYou got it! It took you {} tries.'.format(guess_counter))
            except ValueError:
                print('Only use numbers instead of "{}"!'.format(guess))
                continue


            try:
                new_game = input('Would you like to play again? [y]es/[n]o: ')

                if new_game.lower() == 'y':
                    # Add the number of guesses to the score list
                    scores.append(guess_counter)
                    # Call the function to display the all time highscore
                    print('\n\nThe HIGHSCORE is {}'.format(get_highscore(scores, guess_counter)))

                    # Reset the counter
                    guess_counter = 0
                    random_solution = generate_number()
                    continue
                elif new_game.lower() == 'n':
                    print('\nClosing game, see you next time!')
                    break
                else:
                    raise ValueError('Please type "y" or "n" next time. Exiting...')
                    
            except ValueError as ve:
                print('Oops! {}'.format(ve))
                break

    except KeyboardInterrupt:
        print('User closed game with CTRL+C')
    
                
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()