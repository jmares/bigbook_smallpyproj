# Bagels
# The hexadecimal number version

import random

NUM_DIGITS = 3
MAX_GUESSES = 20

def main():
    print('''Bagels, a deductive logic game.
        By Al Sweigart

I am thinking of a {}-digit hexanumber with no repeated digits.
Hexadecimal: 0 1 2 3 4 5 6 7 8 9 A B C D E F
Try to guess what it is. Here are some clues:
When I say:    That means:
Pico         One digit is correct but in the wrong position.
Fermi        One digit is correct and in the right position.
Bagels       No digit is correct.

For example, if the secret hexanumber was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))

    while True:
        # This stores the secret number the player needs to guess:
        secret_num = get_secret_num()
        print('I have thought up a number.')
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS:
                print('Guess #{}: '.format(num_guesses))
                guess = input('> ').lower()

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break # correct guess
            if num_guesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secret_num))

        # Ask if player wants to play again.
        print('Do you want to play again? (yes or no) ')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def get_secret_num():
    """Returns a string made up of NUM_DIGITS unique random digits"""
    numbers = list('0123456789abcdef')
    random.shuffle(numbers)
    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess, secret_num):
    """Returns a string with the pico, fermi, bagels clues for a guess and secret number pair"""
    if guess == secret_num:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # a correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secret_num:
            # a correct digit is in the wrong place
            clues.append('Pico')
    if len(clues) == 0:
        # There are no correct digits at all
        return 'Bagles'
    else:
        # Sort the clues in alphabetical order so their original order
        # doesn't give information away
        clues.sort()
        # Make a single string from the list of string clues
        return ' '.join(clues)


# If the program is run (instead of imported), run the game
if __name__ == '__main__':
    main()
