import random

class BlackJack(object):
   #setting starting values for the players
    #Creating empty arrays for deck, player_hand and dealer_hand
    deck = []
    player_hand = []
    dealer_hand = []
    player_value = 0
    dealer_value = 0


    def __init__(self):

        # making the deck
        for suit in ['Spade', 'Diamond', 'Club', 'Heart' ]:
            for value in range(2,11):
                self.deck.append( (suit, value, value) )
            for display in ['J', 'Q', 'K']:
                self.deck.append( (suit,display,10) )
            self.deck.append( (suit,'A',11) )
        #shuffling the deck
        random.shuffle(self.deck)
        #starting game
        self.deal_hand()


    def deal_hand(self):
        self.player_hand.append(self.deck.pop(0))
        self.dealer_hand.append(self.deck.pop(0))
        self.player_hand.append(self.deck.pop(0))
        self.dealer_hand.append(self.deck.pop(0))
        self.set_player_value()
        self.set_dealer_value()

        if self.is_blackjack(self.player_value):
            print "Blackjack"
            exit()
        elif self.is_blackjack(self.dealer_value):
            print "Dealer wins"
            exit()
        else:
            self.player_turn()


    def player_turn(self):
        print "Player's Hand"
        print self.player_hand
        print "Total =",self.player_value
        print "Dealer's Hand"
        print self.dealer_hand
        print "Total =",self.dealer_value
        pick = raw_input("Do you want to 'h' or 's'?")
        if pick not in ['h','s']:
            print "Input Invalid please try again"
            self.player_turn()
        elif pick == 'h':
            self.player_hand.append(self.deck.pop(0))
            self.set_player_value()
            print "Player Hand"
            if self.is_blackjack(self.player_value):
                print self.player_hand
                print self.player_value
                print "BlackJack player wins!"

            elif self.is_busted(self.player_value):
                print self.player_hand
                print self.player_value
                print "Busted you lose!"
            else:
                self.player_turn()
        else:
            self.dealer_turn()


    def dealer_turn(self):
        if self.is_deal(self.dealer_value):
            print "Dealer gets additional card"
            self.dealer_hand.append(self.deck.pop(0))
            self.set_dealer_value()
            print "Dealers Hand"
            print "Total", self.dealer_value
            print self.dealer_hand
            if self.is_blackjack(self.dealer_value):
                print "Dealer gets black and wins"
            elif self.is_busted(self.dealer_value):
                print "Dealer busts. Player wins"
            else:
                self.dealer_turn()
        else:
            if int(self.dealer_value) < int(self.player_value):
                print "Player wins"
                exit()
            elif int(self.dealer_value) > int(self.player_value):
                print "Dealer wins"
                exit()
            else:
                print "It's a draw"
                exit()

    def set_player_value(self):
        self.player_value = self.get_hand_value(self.player_hand)


    def set_dealer_value(self):
        self.dealer_value = self.get_hand_value(self.dealer_hand)


    def get_hand_value(self, hand):
        value = 0
        aces = 0
        for s, d, v in hand:
            if d == 'A':
                aces += 1
            if d == 'A' and aces > 1:
                v = 1
            value += v
        if value > 21 and aces != 0:
            value -= 10
        return value

    #If the user gets an ace and the total value is less than than 21 and so the value is 11
    # if the value is over 21 then the ace should be 1
    # if there is more than 1 ace then both should equal 1



    def is_blackjack(self, value):
        return value == 21


    def is_busted(self, value):
        return value >=21


    def is_deal(self, value):
        return value <=16


game = BlackJack()
