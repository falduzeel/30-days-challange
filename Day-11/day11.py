import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
        if rank in ["J", "Q", "K"]:
            self.value = 10
        elif rank == "A":
            self.value = 11
        else:
            self.value = int(rank)

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self, name="Player"):
        self.name = name
        self.cards = []
        self.score = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.score += card.value
        if card.rank == "A":
            self.aces += 1
        self.adjust_for_ace()

    def adjust_for_ace(self):
        while self.score > 21 and self.aces:
            self.score -= 10
            self.aces -= 1

    def show(self, hide_first_card=False):
        if hide_first_card:
            print(f"{self.name}'s Hand: [Hidden Card], {self.cards[1]}")
        else:
            cards_str = ", ".join(str(card) for card in self.cards)
            print(f"{self.name}'s Hand: {cards_str} (Score: {self.score})")

def play_blackjack():
    print("=== Welcome to Day 11: Python Blackjack ===")
    deck = Deck()
    
    player_hand = Hand("Player")
    dealer_hand = Hand("Dealer")

    for _ in range(2):
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())

    dealer_hand.show(hide_first_card=True)
    player_hand.show()

    game_over = False
    while not game_over:
        if player_hand.score == 21:
            print("Blackjack! You hit 21.")
            break
        elif player_hand.score > 21:
            print("Bust! You went over 21.")
            game_over = True
            break
        
        choice = input("Do you want to (H)it or (S)tand? ").strip().upper()
        if choice == 'H':
            player_hand.add_card(deck.deal_card())
            player_hand.show()
        elif choice == 'S':
            break
        else:
            print("Invalid input. Type 'H' or 'S'.")

    if player_hand.score <= 21:
        print("\n--- Dealer's Turn ---")
        dealer_hand.show()
        
        while dealer_hand.score < 17:
            print("Dealer hits...")
            dealer_hand.add_card(deck.deal_card())
            dealer_hand.show()

        print("\n--- Final Results ---")
        player_hand.show()
        dealer_hand.show()

        if dealer_hand.score > 21:
            print("Dealer busted! You win!")
        elif player_hand.score > dealer_hand.score:
            print("You beat the dealer! You win!")
        elif player_hand.score < dealer_hand.score:
            print("Dealer wins!")
        else:
            print("It's a push (Tie)!")

if __name__ == "__main__":
    play_blackjack()