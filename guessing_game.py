"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random
from typing import List

scores: List[int] = []

def generate_number():
    """ Generate a random number between 1 and 10 """
    return random.randint(1, 10)

def get_highscore(attempts_list: List[int], counter: int) -> int:
    """ 
    This function takes the list of attempts 
    and the current state of the guess counter.
    It will return only the lowest amount of attempts.
    """
    highscore = 0
    for attempt in attempts_list:
        if attempt <= counter:
            highscore = attempt
        else:
            highscore = counter

    return highscore


def start_game():
    """
    This program will welcome the User upon starting the game.
    It will utilize two different functions, one for random number
    generation, and one for calculating the highscore.

    The input data will be validated against type and value errors
    throughout the game, and also handeld accordingly.

    The user will be prompted for input as long as he is not guessing
    the randomly generated number. The program will keep count of the
    attempts, and cleares this value if the user decides to play again.
    In that case only the best attempt is shown.

    If the player quits the game, a farewell messages is printed out.
    If the player does not want to finish the game, the program can be
    stopped by pressing CTRL + C. 
    """
    guess_counter = 0
    print('-' * 38 + '\n Welcome to the Number Guessing Game!\n' + '-' * 38 + '\n')

    if guess_counter == 0:
        print('Current HIGHSCORE: You need to play first!')
    random_solution = generate_number()

    try:
        while random_solution:
            try:
                guess: int = input('Pick a number between 1 and 10: ')
                guess = int(guess)
                guess_counter += 1
                print(f'guesses :: #{guess_counter}')      # to debug guesses
                print(f'list-length :: [{len(scores)}] -> {scores}')   # to debug list
                
                if guess < 1 or guess > 10:
                    print('{} is out of range [1-10]. Try again...'.format(guess))
                    guess_counter -= 1
                    continue
                elif guess < random_solution:
                    print('It is higher!')
                    continue
                elif guess > random_solution:
                    print('It is lower!')
                    continue
                else:
                    print('\nYou got it! It took you {} tries.'.format(guess_counter))
                    if not len(scores):
                        print('Best attempt sofar is {}'.format(guess_counter))
                    else:
                        print('Best attempt sofar is {}'.format(get_highscore(scores, guess_counter)))
            except ValueError:
                print('Only use numbers instead of "{}"!'.format(guess))
                continue


            try:
                new_game = input('Would you like to play again? [y]es/[n]o: ')

                if new_game.lower() == 'y':
                    scores.append(guess_counter)
                    print('\n\nThe HIGHSCORE is {}'.format(get_highscore(scores, guess_counter)))
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