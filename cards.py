import random
from constants import colors, values
from players import Player

def generate_deck(Rainbow=False, shuffle = True):
    deck = []
    for color in colors:
        if color == "Rainbow" and not Rainbow:
            continue
        for value in values:
            deck.append((color, value))
    if shuffle:
        random.shuffle(deck)
    return deck

def main():
    print("Testing cards")
    deck = generate_deck(False, False)
    #print(len(deck))
    P1 = Player("Player 1", 3, deck)
    #print(len(deck))
    P2 = Player("Player 2", 3, deck)
    #print(P1.cards, "\n", P1.knowledge)
    P2.give_hint(P1, "white")
    #print("After hint", P1.knowledge)
    discard = []
    print(P1, discard)
    P1.discard(1, deck, discard)
    print(P1, discard)
    

if __name__ == "__main__":
    main()