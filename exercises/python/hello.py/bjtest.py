import random

class BlackJack:
    deck = []
    player_hand = []
    dealer_hand = []
    player_value = 0
    dealer_value = 0


    def __init__(self):
        print '*' * 60
        print ' Welcome to Black Jack'
        print '*' * 60

        # Initialize deck
        for suit in ['Heart','Club','Diamond','Spade']:
            for value in range(2,11):
                self.deck.append( (suit,value,value) )
            for display in ['J','Q','K']:
                self.deck.append( (suit,display,10) )
            self.deck.append( (suit,'A',11) )

        # Shuffle deck
        random.shuffle(self.deck)
        # print self.deck

        self.deal_hands()


    def deal_hands(self):
        self.player_hand.append(self.deck.pop(0))
        self.dealer_hand.append(self.deck.pop(0))
        self.player_hand.append(self.deck.pop(0))
        self.dealer_hand.append(self.deck.pop(0))

        self.set_player_value()
        self.set_dealer_value()

        if self.is_blackjack(self.player_value):
            self.gameover('Player','BlackJack','Won')
        elif self.is_blackjack(self.dealer_value):
            self.gameover('Dealer','BlackJack','Lost')
        else:
            print ' Player\'s Turn'
            print '*' * 60
            self.player_turn()


    def player_turn(self):
        print self
        choice = raw_input(' >> Would you like to hit (h) or stand (s)? ')
        print '*' * 60
        if choice not in ['h','s']:
            print ' >> Wrong input, try again'
            print '*' * 60
            self.player_turn()
        elif choice == 's':
            print ' Dealer\'s Turn'
            print '*' * 60
            self.dealer_turn()
        else:
            self.player_hand.append(self.deck.pop(0))
            self.set_player_value()
            if self.is_blackjack(self.player_value):
                self.gameover('Player','BlackJack','Won')
            elif self.is_busted(self.player_value):
                self.gameover('Player','Busted','Lost')
            else:
                self.player_turn()


    def dealer_turn(self):
        print self
        # Dealer's value <= 16
        if self.is_dealer_hit(self.dealer_value):
            print ' Dealer Hit'
            print '*' * 60
            self.dealer_hand.append(self.deck.pop(0))
            self.set_dealer_value()
            if self.is_blackjack(self.dealer_value):
                self.gameover('Dealer','BlackJack','Lost')
            elif self.is_busted(self.dealer_value):
                self.gameover('Dealer','Busted','Won')
            else:
                self.dealer_turn()
        # Dealer's value > 16 and < 21
        else:
            print ' Dealer Stand'
            print '*' * 60
            if self.dealer_value > self.player_value:
                self.gameover('Dealer','has higher points','Lost')
            elif self.dealer_value < self.player_value:
                self.gameover('Player','has higher points','Won')
            else:
                self.gameover('Dealer/Player','have the same points','Tied')


    def set_player_value(self):
        self.player_value = self.get_hand_value(self.player_hand)


    def set_dealer_value(self):
        self.dealer_value = self.get_hand_value(self.dealer_hand)


    def get_hand_value(self,hand):
        value = 0
        aces = 0
        for s,d,v in hand:
            if d == 'A':
                aces += 1
            if aces > 1:
                v = 1
            value += v
        if value > 21 and aces != 0:
            value -= 10
        return value


    def is_blackjack(self,value):
        return value == 21


    def is_busted(self,value):
        return value > 21


    def is_dealer_hit(self,value):
        return value <= 16


    def gameover(self,side,message,status):
        print self
        print ' >> %s %s.  You %s!' % (side,message,status)
        print '*' * 60
        exit()


    def __repr__(self):
        tpl = ''' Cards remaining: {}
 Dealer's hand: {} = {}
 Player's hand: {} = {}
************************************************************'''
        return tpl.format(len(self.deck),self.dealer_hand,self.dealer_value,self.player_hand,self.player_value)


game = BlackJack()