#!/usr/bin/env python3

import pandas as pd
import random

class Game(object):

    

    def __init__(self, player1, player2, draft='random'):
        
        units = {
            'crossbowman' : 5,
            'royal-guard' : 5,
            'mercenary' : 5,
            'lancer' : 4,
            'marshall' : 5,
            'cavalry' : 4,
            'pikeman' : 4,
            'ensign' : 5,
            'light-cavalry' : 5,
            'berserker' : 5,
            'archer' : 4,
            'footman' : 5,
            'knight' : 4,
            'swordsman' : 5,
            'warrior-priest' : 4
            }
        
        self.bases = [
            (-3, -1, -2),
            (-2, -3, 1),
            (-2, 1, -3),
            (-1, 0, -1),
            (0, -2, 2),
            (0, 2, -2),
            (1, 0, 1),
            (2, -1, 3),
            (2, 3, -1),
            (3, 1, 2)]
        
        # When a base is taken
        # remove it from the adversory's list
        # add it to the player's list
        # if length of player's list == 6 => WIN
        
        self.w_bases = self.bases[:2]
        self.b_bases = self.bases[-2:]
        self.board = {(x-3, y-3, x-y) for x in range(7) for y in range(7) if abs(x-y) <=3}

        # make draft
        if draft == 'random':
            units_draft = random.sample(list(units), 8)
            player1.set_unit_draft(units_draft[:4])
            player2.set_unit_draft(units_draft[-4:])
        else:
            assert(draft == 'random'), "Manual draft not yet implemented"

        # initialize supply
        player1.set_supply(units, player1.unit_draft)


        # Set initiative
        self.initiative = random.randint(0, 1) # 0: Player 2 has initiative
        self.player_turn = self.initiative
        self.state = 'hand'

    def proceed_game(self, last_state):
    #def next_turn ?(self, ):
        while(1):
            if self.state == 'hand':
                pass
                # check if any hand is empty
                # if empty, move to bag
                # else move to initiative
            elif self.state == 'bag':
                pass
                # check if bag is empty
                # if empty, fill the bag with discard
                # else move to initiative
            elif self.state == 'initiative':
                self.player_turn = self.initiative
                self.state = 'play'
            elif self.state == 'draw':
                pass
            elif self.state == 'play':
                self.state = 'win'
                # turn is played outside this module
                return self.player_turn
            elif self.state == 'win':
                if self.player_turn == self.initiative:
                    self.player_turn = not self.player_turn
                    self.state ='play'
                else:
                    self.state = 'hand'

    def _load_units(self):
        filename = '../resources/units.csv'
        try:
            self.units = pd.read_csv(filename, sep='\t')
        except:
            print("units.csv file was not found.")

    def _random_unit_draft(self, remaining_units={}):
        if len(remaining_units) == 0:
            remaining_units = self.units
        units_draft = random.sample(remaining_units, 4)
        remaining_units = [unit for unit in self.units if unit not in units_draft]
        return (units_draft, remaining_units)

    # other function interacting with players ?

class Player(object):

    def __init__(self):
        self.unit_draft = []
        self.hand = []
        self.supply = {}
        self.discard = []
        self.eliminated = []
        self.bag = ['royal-coin']

    def set_unit_draft(self, unit_list):
        self.unit_draft = unit_list

    def set_supply(self, units, unit_draft):
        set.supply = {k:v-2 for k,v in units.items() if k in unit_draft}
    
    def set_bag(self, unit_draft):
        for unit in unit_draft:
            self.bag += list(unit) * 2

    def draw(self):
        hand_size = 0
        while hand_size < 3:
            if self.bag == []:
                self.bag = self.discard
                self.discard = []
            else:
                if self.discard == []:
                    break
                else:
                    self.hand += random.sample(self.bag, 1)
                    hand_size += 1

    def make_action(self):
        pass

    def get_open_moves(self):
        pass
