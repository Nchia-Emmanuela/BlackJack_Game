import random
from arts import logo

def random_card():
    """Returns a random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(card)
    return card

def calc_score(cards):
    """Takes a list of card and returns the sum of all items in the card"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards ) > 21:
        cards.remove(11)
        cards.append(1)
    sum(cards)

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