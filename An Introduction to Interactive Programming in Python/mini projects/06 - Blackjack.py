# Mini-project #6 - Blackjack http://www.codeskulptor.org/#user40_qg8WJqrNOJ_1.py

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        return "Hand contains " + ' '.join([card.get_suit() + card.get_rank() for card in self.hand])

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
    	hand_value = 0
        ace = False
        for card in self.hand:
            rank = card.get_rank()
            hand_value += VALUES[rank]
            if rank == 'A':
                ace = True
        if ace and hand_value + 10 <= 21:
            hand_value += 10
        return hand_value
   
    def draw(self, canvas, pos):
        pass	# draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = [Card(suit, rank) for rank in RANKS for suit in SUITS]

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)
        return self.deck

    def deal_card(self):
        return self.deck.pop()
    
    def __str__(self):
        return "Deck contains " + ' '.join([card.get_suit() + card.get_rank() for card in self.deck])



#define event handlers for buttons
def deal():
    global outcome, in_play

    player = Hand()
    dealer = Hand()
    
    deck = Deck()
    deck.shuffle()
    
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    
    print "Player" , player
    print "Dealer" , dealer
    
    in_play = True

def hit():
    global outcome, in_play, score

    if in_play:
        if player.get_value() <= 21:
            player.add_card(deck.deal_card())

        if player.get_value() > 21:
            print "You have busted"
            in_play = False
   
        print "Player", player, "=>", player.get_value()
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome, in_play, score
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        print "Dealer", dealer, "=>", dealer.get_value()
        if dealer.get_value() > 21:
            print "Dealer has busted"
            in_play = False
        else:
            if (player.get_value() <= dealer.get_value()):
                print "Dealer Wins"
            else:
                print "You Win"
    else:
        print "You have busted"

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    card = Card("S", "A")
    card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric