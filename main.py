import random
import os
from arts import logo

def clear(): 
    os.system('cls')

def random_card():
    """Returns a random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calc_score(cards):
    """Takes a list of card and returns the sum of all items in the card"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards ) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(players_score, computers_score):
    if players_score == computers_score:
        return "Draw"
    elif computers_score == 0:
        return "Lose, opponent has BlackJack 😱"
    elif players_score == 0:
        return "Win, with a BlackJack 😎"
    elif players_score > 21:
        return "You went over, you lose 😥"
    elif computers_score > 21:
        return "Opponent went over, you win 😀"
    elif players_score > computers_score:
        return "You win😃😀"
    else:
        return "You lose😥"
def play_game():
    print(logo)
    player_cards = []
    computer_card = []

    is_game_over = False

    for i in range(2):
        player_cards.append(random_card())
        computer_card.append(random_card())


    while not is_game_over:
        players_score = calc_score(player_cards)
        computers_score = calc_score(computer_card)
        print(f"your cards: {player_cards}, current score: {players_score}")
        print(f"Computer's first card: {computer_card[0]}, current score: {computers_score}")

        if players_score == 0 or computers_score == 0 or players_score > 21:
            is_game_over = True
        else:
            take_card = input("type y to take another card type n to pass: ")
            if take_card == "y":
                player_cards.append(random_card())
            else:
                is_game_over = True

    while computers_score != 0 and computers_score < 17:
        computer_card.append(random_card())
        computers_score = calc_score(computer_card)

    print(f"your final hand : {player_cards}, final score: {players_score}")
    print(f"Computers final hand : {computer_card}, final score: {computers_score}")
    print(compare(players_score, computers_score))

while input("Do you want to play the BlackJack game? type y or n: ") == "y":
    clear()
    play_game()