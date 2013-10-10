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

        random.shuffle(self.deck)
        self.deal_hand()
        # print self.player_hand
        # print self.dealer_hand



    def deal_hand(self):
        self.player_hand.append(self.deck.pop(0))
        self.dealer_hand.append(self.deck.pop(0))
        self.player_hand.append(self.deck.pop(0))
        self.dealer_hand.append(self.deck.pop(0))
        # self.player_value()
        # self.dealer_value()
        self.player_turn()



    def player_turn(self):
        print "Player's cards"
        print self.player_hand
        self.player_val = self.player_hand[0][2]+ self.player_hand[1][2]
        print self.player_val
        if self.player_val == 21:
            print "Blackjack"

        elif self.player_val < 21:
            answer = raw_input("Do you want to hit or stand?")
            if answer == 'hit':
                self.player_hand.append(self.deck.pop(0))
                print self.player_hand
                self.player_val = self.player_hand[0][2]+ self.player_hand[1][2]+ self.player_hand[2][2]
                print self.player_val
                self.dealer_turn()
            elif answer == 'stand':
                self.dealer_turn()
            elif answer not in ['stand','hit']:
                print ' >> Wrong input, try again'
                self.player_turn()
            else:
                pass


            # answer2 = raw_input("Do you want to hit or stand?")

        # print self.player_value == 21:
        #     print "Blackjack"
        # elif self.player_value <= 20:
        #     self.player_hand.append(self.deck.pop(0))
        # self.dealer_turn()


    def dealer_turn(self):
        print "Dealer's cards"
        print self.dealer_hand
        print self.player_val


    # def player_value(self):
    #     self.player_value = self.get_hand_value(self.player_hand)
    #
    #
    # def dealer_value(self):
    #     self.player_value = self.get_hand_value(self.dealer_hand)
    #
    #
    # def get_hand_value(self, hand):
    #     value = 0
    #     for s, d, v in hand:
    #         value += v
    #     return value


        # if dealer_val <= 16:
        #     self.dealer_hand.append(self.deck.pop(0))
        # elif dealer_val > 16:
        #     pass
        # elif dealer_val == 21:
        #     self.winner()
        # else dealer_val > 21:
        #     print "Dealer Loses"


    # def win(self):
    #     if player




    def bust(self):
        print "You Busted"
        self.dealer_hand()





game = BlackJack()
