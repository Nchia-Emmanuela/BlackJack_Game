import random
from arts import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def random_card():
    selected_cards =[]
    for i in range(0, 2):
        random_point= random.randint(0, len(cards)-1)
        picked_card = cards[random_point]
        selected_cards.append(picked_card)
    return selected_cards

players_card = random_card()
score = players_card[0] + players_card[1]
print(f"your current cards: {players_card}, current score: {score}")

computers_card = random_card()
print(f"Computer's first card: {computers_card[0]}")
