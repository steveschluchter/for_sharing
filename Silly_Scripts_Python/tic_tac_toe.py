#!/usr/bin/python3

# This program is a place for two people to play tic-tac-toe against eachother.
# Author: Steve Schluchter
# Date: 13.March.2023
# This program has no dependencies other than Python 3.x.
# To run this program, simply execute the shell command 'python tic_tac_toe.py'. 


TIC_TAC_TOE_TEXT = """___________.__         ___________               ___________          ._.
\__    ___/|__| ____   \__    ___/____    ____   \__    ___/___   ____| |
  |    |   |  |/ ___\    |    |  \__  \ _/ ___\    |    | /  _ \_/ __ \ |
  |    |   |  \  \___    |    |   / __ \\  \___    |    |(  <_> )  ___/\|
  |____|   |__|\___  >   |____|  (____  /\___  >   |____| \____/ \___  >_
                   \/                 \/     \/                      \/\/"""


class tic_tac_toe_game():

    def __init__(self):

        #a list of tuples that will enumerate which 
        
        self.x_turn = True 
        self.game_on = True 
        self.turn_count = 1
        self.plays_made = {}
        self.board =  [       ['-', '-', '-', '-','-','-','-','-','-','-','-',"\n"],
                              ['1', ' ', ' ', '|','2',' ',' ','|','3',' ',' ',"\n"],
                              [' ', ' ', ' ', '|',' ',' ',' ','|',' ',' ',' ',"\n"],
                              [' ', ' ', ' ', '|',' ',' ',' ','|',' ',' ',' ',"\n"],
                              ['-', '-', '-', '-','-','-','-','-','-','-','-',"\n"],
                              ['4', ' ', ' ', '|','5',' ',' ','|','6',' ',' ',"\n"],
                              [' ', ' ', ' ', '|',' ',' ',' ','|',' ',' ',' ',"\n"],
                              [' ', ' ', ' ', '|',' ',' ',' ','|',' ',' ',' ',"\n"],
                              ['-', '-', '-', '-','-','-','-','-','-','-','-',"\n"],
                              ['7', ' ', ' ', '|','8',' ',' ','|','9',' ',' ',"\n"],
                              [' ', ' ', ' ', '|',' ',' ',' ','|',' ',' ',' ',"\n"],
                              [' ', ' ', ' ', '|',' ',' ',' ','|',' ',' ',' ',"\n"],
                              ['-', '-', '-', '-','-','-','-','-','-','-','-',"\n"]]

    #print the board to the screen
    def print_board(self):
   
        board_data = []

        for i in range(0,9):
            board_data.append(' ')

        for i in self.plays_made.keys():
            board_data[i-1] = self.plays_made[i][0]

        board_copy = []
        
        for i in range(0,13):

            board_copy.append(self.board[i].copy())

        board_copy[2][1] = board_data[0]
        board_copy[2][5] = board_data[1]
        board_copy[2][9] = board_data[2]
        board_copy[6][1] = board_data[3]
        board_copy[6][5] = board_data[4]
        board_copy[6][9] = board_data[5]
        board_copy[10][1] = board_data[6]
        board_copy[10][5] = board_data[7]
        board_copy[10][9] = board_data[8]

        for row in board_copy:

            for character in row:

                print(character, end='')


    def prompt_user(self):

        return_this = ""

        if self.x_turn:

            print("X, pick a square.")

        else:

            print("O, pick a square.")

        while True:
           
            return_this = input("Enter a integer in the interval [0, 9]. ")
           
            if return_this in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']: 
                
                break

            else:

                continue

        return int(return_this)

    #adds a turn taken to the record of what's been played
    def add_turn(self, square):

        turn_data = []

        if self.x_turn == True:
        
            turn_data.append('X')

        else:

            turn_data.append('0')

        turn_data.append(self.turn_count)
        self.plays_made[i] =turn_data

        #iterate bookkeepers for next turn
        self.turn_count += 1
        self.x_turn = not self.x_turn

    #checks for a winner or a tie game
    def is_game_over(self):

        keys = self.plays_made.keys()

        if 5 in keys:
            
            print(self.plays_made[5][0])


            if  (4 in keys) and (6 in keys):

                if self.plays_made[5][0] == self.plays_made[4][0] and self.plays_made[5][0] == self.plays_made[6][0]:

                    return True

            if  (3 in keys) and (7 in keys):
                
                if self.plays_made[3][0] == self.plays_made[5][0] and self.plays_made[5][0] == self.plays_made[7][0]:

                    return True

            if (1 in keys) and (9 in keys):

                                
                print(self.plays_made[5][0] == self.plays_made[1][0])
                if self.plays_made[1][0] == self.plays_made[5][0] and self.plays_made[5][0] == self.plays_made[9][0]:

                    return True

            if (2 in keys) and (8 in keys):
                 
                if self.plays_made[2][0] == self.plays_made[5][0] and self.plays_made[5][0] == self.plays_made[8][0]:

                    return True

        elif 1 in keys:

            if (4 in keys) and (7 in keys):

                if self.plays_made[1][0] == self.plays_made[4][0] and self.plays_made[4][0] == self.plays_made[7][0]:

                    return True

            if (2 in keys) and (3 in keys):
                 
                if self.plays_made[1][0] == self.plays_made[2][0] and self.plays_made[2][0] == self.plays_made[3][0]:

                    return True

        elif 9 in keys:

            if (3 in keys) and (6 in keys):
                
                if self.plays_made[3][0] == self.plays_made[6][0] and self.plays_made[6][0] == self.plays_made[9][0]:

                    return True

            if (7 in keys) and (9 in keys):
                        
                if self.plays_made[7][0] == self.plays_made[8][0] and self.plays_made[8][0] == self.plays_made[9][0]:

                    return True

        return False
        

if __name__ == '__main__':

    print(TIC_TAC_TOE_TEXT)

    new_game = tic_tac_toe_game()

    while new_game.game_on == True:

        new_game.print_board() 
        i = new_game.prompt_user()        

        if i in new_game.plays_made.keys():

            print("That square is taken.")
            continue

        new_game.add_turn(i)
        if (new_game.is_game_over()):

            print("GAME OVER")
            
            new_game.game_on = False

            if not new_game.x_turn:

                print("X WINS")

            else:

                print("O WINS")

    print("End program.")
