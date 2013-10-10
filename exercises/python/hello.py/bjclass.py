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