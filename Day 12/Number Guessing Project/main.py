from random import randint
from art import logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
# function to check user's against actual answer
def check_answer(user_guess,actual_answer, turns):
    '''check user's against actual answer'''
    if user_guess > actual_answer:
        print('Too high.')
        return turns - 1
    elif user_guess < actual_answer:
        print('Too low.')
        return turns -1
    else:
        print(f'You got it! the answer was {actual_answer}')

#function to get difficulty

def set_difficulty():
    level = input('choose a difficulty. Type "easy" or "hard": ').lower()
    if level == 'easy':
        return  EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
# turns = set_difficulty()
# print(f"You have {turns} attempts remaining to guess the number.")

def game():
    print(logo)
    # Choosing a random number between 1 and 100
    print('Welcome to the guessing number')
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1,100)

    turns = set_difficulty()
    #let the user guess a number
    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print('you have run out of guessing, you lose')
            print(f'Pssst, the correct answer is {answer}')
            return
        elif guess != answer:
            print('guess again.')
game()



# track the number of turns and reduce by 1 if they get it wrong

# repeat the guessing functionality if they get it wrong.

