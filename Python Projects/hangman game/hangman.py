"""
File: hangman.py
Name: Athena
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random

N_TURNS = 7     # Controls how many chances the user have to guess


def main():
    """
    This program will randomly come up with a vocabulary,
    and the user can pick either one of the 26 alphabets for a guess.
    If the alphabet you pick is in the vocabulary, this program will
    show you the relative position(s) of the alphabet. If not,
    you lose one guess.(You have N_TURNS guesses.)
    The game ends either you guess all the alphabets right(win) or used up all 7 guesses(lose.)
    """
    ans = random_word()
    n_turns = N_TURNS

    dashed_ans = ''
    for i in range(len(ans)):
        dashed_ans += '-'

    print('The word looks like: ' + dashed_ans)
    print('You have ' + str(n_turns) + ' wrong guesses left.')

    while True:
        guess = input('Your guess: ').upper()

        if not guess.isalpha() or len(guess) != 1:
            print('Illegal format.')
        else:
            if guess in ans:
                print('You are correct!')
                new_dashed_ans = ''
                for i in range(len(dashed_ans)):
                    if ans[i] == guess:
                        new_dashed_ans += guess
                    else:
                        new_dashed_ans += dashed_ans[i]

                dashed_ans = new_dashed_ans
            else:
                # Update n_turns
                n_turns -= 1
                print('There is no ' + guess + '\'s in the word.')

            if n_turns == 0:
                print('You are completely hung :(')
                break
            if '-' not in dashed_ans:
                print('You win!!')
                break

            print('The word looks like: ' + dashed_ans)
            print('You have ' + str(n_turns) + ' wrong guesses left.')

    print('The answer is: ' + ans)


def random_word():
    """
    To pick a random answer.
    return: str, the answer picked.
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


if __name__ == '__main__':
    main()

