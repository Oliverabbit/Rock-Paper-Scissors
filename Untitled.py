#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


class ReapetPlayer(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        p = random.choice(moves)
        return (p)


class ReflectPlayer(Player):
    def __init__(self):
        self.x = 0

    def move(self):
        if self.x == 0:
            self.x += 1
            return 'rock'
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        if self.x > 0:
            self.my_move = my_move
            self.their_move = my_move


class CyclePlayer(Player):
    def __init__(self):
        self.x = 0

    def move(self):
        if self.x == 0:
            self.x += 1
            return 'rock'
        elif self.x == 1:
            self.x += 1
            return 'paper'
        elif self.x == 2:
            self.x -= 2
            return 'scissors'


class HumanPlayer(Player):
    def move(self):
        user_entry = input("Pleas enter your move (rock, paper, scissors)?")
        while user_entry not in moves:
            user_entry = input('Try Again')
        return user_entry


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.player_one_score = 0
        self.player_two_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.p1.learn(move2, move1)
        self.p2.learn(move1, move2)
        print(f"Player1 = {move1}, Player2 = {move2}")
        Game.beats(self, move1, move2)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
            if self.player_one_score == self.player_two_score:
                print(f"score P1= {self.player_one_score}, \
                P2= {self.player_two_score}")
                print('its a tie')
                print('No winners')
            elif self.player_one_score > self.player_two_score:
                print(f"score P1= {self.player_one_score}, \
                P2= {self.player_two_score}")
                print('Congratulations to Player 1')
            elif self.player_one_score < self.player_two_score:
                print(f"score P1= {self.player_one_score}, \
                P2= {self.player_two_score}")
                print('Congratulations to Player 2')
        print('Finl score = Player1 = ' + str(self.player_one_score))
        print(' , Player2 = ' + str(self.player_two_score))
        print("Game over!")

    def beats(self, one, two):
        global player_one_score
        global player_two_score
        if ((one == 'rock' and two == 'scissors') or
           (one == 'scissors' and two == 'paper') or
           (one == 'paper' and two == 'rock')):
            self.player_one_score += 1
        if ((two == 'rock' and one == 'scissors') or
           (two == 'scissors' and one == 'paper') or
           (two == 'paper' and one == 'rock')):
            self.player_two_score += 1


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
