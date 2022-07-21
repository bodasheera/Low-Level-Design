"""
Create a snake and ladder application.

The application should take as input (from the command line or a file):

- Number of snakes (s) followed by s lines each containing 2 numbers denoting the head and tail positions of the snake.

- Number of ladders (l) followed by l lines each containing 2 numbers denoting the start and end positions of the ladder.

- Number of players (p) followed by p lines each containing a name.

After taking these inputs, you should print all the moves in the form of the current player name followed by a random number between 1 to 6 denoting the die roll and the initial and final position based on the move.
Format: <player_name> rolled a <dice_value> and moved from <initial_position> to <final_position>

When someone wins the game, print that the player won the game.
Format: <player_name> wins the game

Rules of the game

- The board will have 100 cells numbered from 1 to 100.

- The game will have a six sided dice numbered from 1 to 6 and will always give a random number on rolling it.

- Each player has a piece which is initially kept outside the board (i.e., at position 0).

- Each player rolls the dice when their turn comes.

- Based on the dice value, the player moves their piece forward that number of cells. Ex: If the dice value is 5 and the piece is at position 21, the player will put their piece at position 26 now (21+5).

- A player wins if it exactly reaches the position 100 and the game ends there.

- After the dice roll, if a piece is supposed to move outside position 100, it does not move.

- The board also contains some snakes and ladders.

- Each snake will have its head at some number and its tail at a smaller number.

- Whenever a piece ends up at a position with the head of the snake, the piece should go down to the position of the tail of that snake.

- Each ladder will have its start position at some number and end position at a larger number.

- Whenever a piece ends up at a position with the start of the ladder, the piece should go up to the position of the end of that ladder.

- There could be another snake/ladder at the tail of the snake or the end position of the ladder and the piece should go up/down accordingly.

Assumptions you can take apart from those already mentioned in rules

- There won’t be a snake at 100.

- There won’t be multiple snakes/ladders at the same start/head point.

- It is possible to reach 100, i.e., it is possible to win the game.

- Snakes and Ladders do not form an infinite loop.

Optional Requirements

Please do these only if you’ve time left. You can write your code such that these could be accommodated without changing your code much.

The game is played with two dice instead of 1 and so the total dice value could be between 2 to 12 in a single move.
The board size can be customizable and can be taken as input before other input (snakes, ladders, players).
In case of more than 2 players, the game continues until only one player is left.
On getting a 6, you get another turn and on getting 3 consecutive 6s, all the three of those get cancelled.
On starting the application, the snakes and ladders should be created programmatically without any user input, keeping in mind the constraints mentioned in rules.
There could be different ways to design a solution for this. I’ll mention how I would have approached it during an actual interview.

Let’s dissect the problem statement to determine how to design a good solution for it.

The gist of the problem statement is that we need to create a snake and ladder game. The game will have multiple snakes and ladders and there will be multiple people playing the game. The game is played automatically based on certain rules and ends when a player wins.

"""


"""

Board 
Snake
Ladder 
Dice 
Players

"""


from random import randint, random
from typing import List, final


class Range:
    start: int
    end: int

    def __init__(self,start,end) -> None:
        self.start = start
        self.end = end


class Snakes:

    snakes: List[Range]

    def __init__(self) -> None:
        self.snakes = []
    
    def add_snakes(self):
        num_snakes = int(input("Number of Snakes "))
        for i in range(num_snakes):
            head = tail = 0
            head,tail =  map(int, input(f"Enter head and tail for snake {i+1} ").split())
            self.snakes.append(Range(head,tail))

    def if_snake(self,pos):
        f = -1
        for i in self.snakes:
            if i.start == pos:
                f = i.end
                print(f" Oops !! Snake will move you to {i.end}")
        return f


class Ladders:

    ladders: List[Range]

    def __init__(self) -> None:
        self.ladders = []
    
    def add_ladders(self):
        num_ladders = int(input("Number of Ladders "))
        for i in range(num_ladders):
            start = end = 0
            while True:
                start,end =  map(int, input(f"Enter start and end for ladder {i+1} ").split())
                if start and end and end > start :
                    break
            self.ladders.append(Range(start,end))

    def if_ladder(self,pos):
        f = -1
        for i in self.ladders:
            if i.start == pos:
                f = i.end
                print(f" W ohoo !! Ladder will move you to {i.end}")

        return f
    

class Player:
    name: str
    position: int 
    next: any

    def __init__(self,name) -> None:
        self.name = name
        self.position = 0
        self.next = None
    

class Players:
    players: List[Player]
    current_index: int

    def __init__(self) -> None:
        self.players = []
        self.current_index = 0

    def add_players(self):
        num_players = int(input("Number of Players "))
        for _ in range(num_players): 
            name = input("Enter player name ")
            self.players.append(Player(name))
        self.set_order()

    def set_order(self):
        for i in range(len(self.players)-1):
            self.players[i].next = self.players[i+1]
        self.players[-1].next = self.players[0]

    def next_player(self):
        self.players[self.current_index] = self.players[self.current_index].next


    def update_pos(self,pos):
        self.players[self.current_index].position = pos 


class SnakeAndLadders:

    WINNING_NUMBER = 100
    snakes: Snakes
    ladders: Ladders
    players: Players

    def __init__(self) -> None:
        self.snakes = Snakes()
        self.ladders = Ladders()
        self.players = Players()
        self.snakes.add_snakes()
        self.ladders.add_ladders()
        self.players.add_players()

        self.start_game()


    def play(self):
        dice = randint(0,6)
        print(f"Player {self.players.players[self.players.current_index].name} rolled dice {dice}")
        prev = self.players.players[self.players.current_index].position
        temp_pos = prev + dice

        if temp_pos > 100:
            print(f"Oops ! You need a number less than {100-prev} to win")
            return 
        final_pos = -1
        snake_tail = self.snakes.if_snake(temp_pos)
        if snake_tail != -1:
            self.players.update_pos(snake_tail)
            final_pos = snake_tail
        else:
            ladder_head = self.ladders.if_ladder(temp_pos)
            if ladder_head != -1:
                self.players.update_pos(ladder_head)
                final_pos = ladder_head
            else:
                self.players.update_pos(temp_pos) 
                final_pos = temp_pos

        print(f"Player {self.players.players[self.players.current_index].name} moved from {prev} to {final_pos}")
        print("\n")

    def is_game_over(self):
        return self.players.players[self.players.current_index].position == 100

    def start_game(self):
        while not self.is_game_over():
            self.players.next_player()
            self.play()

        print(f"Congratulations {self.players.players[self.players.current_index].name} !!")


SnakeAndLadders()