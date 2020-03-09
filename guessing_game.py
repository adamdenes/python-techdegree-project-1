"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random


scores = []

def generate_number():
    return random.randint(1, 10)

def get_highscore(attempt):
    pass

def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    print('-' * 38 + '\n Welcome to the Number Guessing Game!\n' + '-' * 38 + '\n')

    random_solution = generate_number()
    guess_counter = 0

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
                    print('\n\nThe HIGHSCORE is {}'.format(guess_counter))
                    guess_counter = 0
                    random_solution = generate_number()
                    continue
                elif new_game.lower() == 'n':
                    print('Closing game, see you next time!')
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