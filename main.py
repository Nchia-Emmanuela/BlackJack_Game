import random
from arts import logo

def random_card():
    """Returns a random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(card)
    return card

player_cards = []
computer_card = []

for i in range(2):
    player_cards.append(random_card())
    computer_card.append(random_card())

def calc_score(cards):
    sum(cards)
