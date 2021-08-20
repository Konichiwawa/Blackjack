import random

# variables for card traits
suits = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

# create a card
class Card():
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank # this works as key to retrive card values from the values dict 
    
    # function to display the card 
    def __str__(self):
        return self.rank + ' of ' + self.suit 
    
# create a deck of cards
class Deck():
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    # function to shuffle the deck 
    def shuffle(self):
        random.shuffle(self.deck)
    
    # function to deal a card from the deck
    def deal(self):
        single_card = self.deck.pop()
        return single_card 
    
# create class object for hand 
class Hand():
    
    def __init__(self):
        self.cards = []
        self.values = 0
        self.aces = 0
    
    # function to accept dealt cards
    def add_card(self, card):
        self.cards.append(card)
        self.values += values[card.rank] 
        if card.rank == 'Ace':
            self.aces += 1
        
    # function to examine Ace cards 
    def ace_card(self):
        while self.values > 21 and self.aces >= 1:
            self.values -= 10
            self.aces -= 1 
            
# creat class object for chips   
class Chips():
    
    def __init__(self):
        self.total = 100 # starts with a max of 100 points
        self.bet = 0 
        
    def win_bet(self):
        self.total += self.bet 
        
    def lose_bet(self):
        self.total -= self.bet 
        
# function to bet the chips 
def bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except:
            print('answer must be an integer')
            continue
        else:
            if chips.bet > chips.total:
                print("Your bet cannot exceed", chips.total)
            else:
                break
       
# function to show all hands expept the dealer        
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" < Card Hidden >")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Total Value =", player.values)

# function to show all hands
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Total value = ", dealer.values)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Total Value =",player.values)

# function to determine player victory 
def player_win(player, dealer, chips):
    if dealer.values > 21:
        print("\nDealer busts!")
        player_chips.win_bet()
            
    elif player.values <= 21 and dealer.values < player.values:
        print("\nPlayer wins!")
        player_chips.win_bet()

# function to determine player loss 
def player_loss(player, dealer, chips):
    if player.values > 21:
        print("\nPlayer busts!")
        player_chips.lose_bet()
        
    elif dealer.values <= 21 and dealer.values > player.values:
        print("\nDealer wins!")
        player_chips.lose_bet()
 
# function to determine tie
def tie(player, dealer):
    if dealer.values == player.values:
        print("\nDealer and Player tie!")

# function to ask for Y or N depending on the quesiton(string)
def ask(string):
    while True:
        try:
            ask = input(f"{string} Y or N: ").upper()
        except:
            print("please enter Y or N")
            continue
        else:
            if ask == 'Y':
                return True
                break
            elif ask == 'N':
                return False 
                break

# game logic
print('Welcome to BlackJack! Get as close to 21 as possbile. Face cards count as 10 and Aces count as 1 or 11.')

play = True

while play:
    
    # Set up the player's chips
    player_chips = Chips() 
    
    while player_chips.total > 1:
    
        # create & shuffle the deck
        deck = Deck()
        deck.shuffle()
        
        # deal two cards to the player & the dealer
        player = Hand()
        player.add_card(deck.deal())
        player.add_card(deck.deal())
        
        dealer = Hand()
        dealer.add_card(deck.deal())
        dealer.add_card(deck.deal())           
        
        bet(player_chips)
        
        show_some(player,dealer)
        
            
        # asks if the player wants additional cards while under 21
        while player.values < 21:
            hit = ask("Would you like to hit / take an additional card?")
            if hit == True:
                player.add_card(deck.deal())
                player.ace_card() 
                show_some(player, dealer)
            else:
                break
            
        # dealer keeps taking cards untill it reaches 17      
        while dealer.values < 17:
            dealer.add_card(deck.deal())
            dealer.ace_card() 
    
        show_all(player,dealer)
            
        # check for win/loss
        player_win(player, dealer, player_chips)
        player_loss(player, dealer, player_chips)
        tie(player, dealer)
        
        # display the amount of chips the player has after each round
        print("Player's current chips amount: ",player_chips.total)
        
        # ask to play again
        keep_going = ask("Would you like to continue playing?")
        if keep_going == True:
            if player_chips.total > 1:
                continue
            else:
                print('You ran out of chips.')
                break
        else:
            player_chips.total = 0
            
    # if the player runs out of the chips            
    if player_chips.total < 1:
        start_over = ask("Would you like to start over?")
        if start_over == True:
            play = True
        else:
            print("Thanks for playing!")
            play = False
  
        
        