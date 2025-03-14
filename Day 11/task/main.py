import random
from art import  logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return  card


def calculate_score(cards):
    '''This function take a list of cards return the score calculated score from the card'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(u_score, c_score):
    if u_score == c_score:
        return "draw"
    elif c_score == 0:
        return "Lose, opponent has Blackjack "
    elif u_score == 0:
        return "You went over. You lose."
    elif c_score > 22:
        return "Opponent went over. You win."
    elif u_score > c_score:
        return "You win."
    else:
        return "You lose."
def game():
    print(logo)
    user_card = []
    computer_card = []
    user_score = -1
    computer_score = -1
    is_game_over = False
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    while not is_game_over:
        user_score  = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"computers first card: {computer_card[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
    print(f'your final hand: {user_card}, final score: {user_score}')
    print(f'computers final hand: {computer_card}, final score: {computer_score}')
    print(compare(user_score,computer_score))

while input('Do you want game? "y" or "n"') == 'y':
    print('\n'*20)
    game()