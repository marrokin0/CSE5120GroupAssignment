"""
PLEASE READ THE COMMENTS BELOW AND THE HOMEWORK DESCRIPTION VERY CAREFULLY BEFORE YOU START CODING

 The file where you will need to create the GUI which should include (i) drawing the grid, (ii) call your Minimax/Negamax functions
 at each step of the game, (iii) allowing the controls on the GUI to be managed (e.g., setting board size, using 
                                                                                 Minimax or Negamax, and other options)
 In the example below, grid creation is supported using pygame which you can use. You are free to use any other 
 library to create better looking GUI with more control. In the __init__ function, GRID_SIZE (Line number 36) is the variable that
 sets the size of the grid. Once you have the Minimax code written in multiAgents.py file, it is recommended to test
 your algorithm (with alpha-beta pruning) on a 3x3 GRID_SIZE to see if the computer always tries for a draw and does 
 not let you win the game. Here is a video tutorial for using pygame to create grids http://youtu.be/mdTeqiWyFnc
 
 
 PLEASE CAREFULLY SEE THE PORTIONS OF THE CODE/FUNCTIONS WHERE IT INDICATES "YOUR CODE BELOW" TO COMPLETE THE SECTIONS
 
"""
import pygame
import numpy as np
from GameStatus_5120 import GameStatus
from multiAgents import minimax, negamax
import sys, random

mode = "player_vs_ai" # default mode for playing the game (player vs AI)

class RandomBoardTicTacToe:
    def __init__(self, size = (600, 600)):

        self.size = self.width, self.height = size
        # Define some colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)

        # Grid Size
        self.GRID_SIZE = 4
        self. OFFSET = 5

        self.CIRCLE_COLOR = (140, 146, 172)
        self.CROSS_COLOR = (140, 146, 172)

        # This sets the WIDTH and HEIGHT of each grid location
        self.WIDTH = self.size[0]/self.GRID_SIZE - self.OFFSET
        self.HEIGHT = self.size[1]/self.GRID_SIZE - self.OFFSET

        # This sets the margin between each cell
        self.MARGIN = 5

        # Initialize pygame
        pygame.init()
        self.game_reset()

    def draw_game(self):
        # Create a 2 dimensional array using the column and row variables
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Tic Tac Toe Random Grid")
        self.screen.fill(self.BLACK)
        # Draw the grid
        for x in range(self.GRID_SIZE):
            for y in range(self.GRID_SIZE):
                rect = pygame.Rect(
                    (self.MARGIN + self.WIDTH) * y + self.MARGIN,
                    (self.MARGIN + self.HEIGHT) * x +self.MARGIN,
                    self.WIDTH, self.HEIGHT
                )
                pygame.draw.rect(self.screen, self.WHITE, rect)
        pygame.display.update()

    def change_turn(self):

        if(self.game_state.turn_O):
            pygame.display.set_caption("Tic Tac Toe - O's turn")
        else:
            pygame.display.set_caption("Tic Tac Toe - X's turn")

    def draw_circle(self, x, y):
        center = ((self.MARGIN + self.WIDTH) * y + self.MARGIN + self.WIDTH /2, 
                  (self.MARGIN + self.HEIGHT) * x + self.MARGIN + self.HEIGHT /2
        )
        radius = min(self.WIDTH, self.HEIGHT) / 2 - self.OFFSET
        pygame.draw.circle(self.screen, self.CIRCLE_COLOR, center, radius, 5)
        pygame.display.update()

    def draw_cross(self, x, y):
        start_position1 = ((self.MARGIN + self.WIDTH) * y + self.MARGIN + self.OFFSET, 
                           (self.MARGIN + self.HEIGHT) * x + self.MARGIN + self.OFFSET
        )
        end_position1 = ((self.MARGIN + self.WIDTH) * (y + 1) - self.MARGIN - self.OFFSET, 
                         (self.MARGIN + self.HEIGHT) * (x + 1) - self.MARGIN - self.OFFSET
        )
        start_position2 = ((self.MARGIN + self.WIDTH) * (y + 1) - self.MARGIN - self.OFFSET, 
                           (self.MARGIN + self.HEIGHT) * x + self.MARGIN + self.OFFSET
        )
        end_position2 = ((self.MARGIN + self.WIDTH) * y + self.MARGIN + self.OFFSET, 
                         (self.MARGIN + self.HEIGHT) * (x + 1) - self.MARGIN - self.OFFSET
        )

    def is_game_over(self):
        if self.game_state.is_terminal():
            return True

    def move(self, move):
        self.game_state = self.game_state.get_new_state(move)


    def play_ai(self):
        # Adjust depth on the number of empty cells
        if empty_cells = sum(x.count(0) for x in self.game_state.board_state)
            depth = 6 # 3x3 board
        elif empty_cells > 16:
            depth = 4 # Large boards with lots of empty cells
        else:
            depth = 6 # Increase depth as the board gets filled

        # Use selected AI Algorithm
        if self.ai_choice == 'minimax':
            eval_score, move = minimax(self.game_state, depth=depth, maximizingPlayer=(self.ai_symbol == 'O'))
        elif self.ai_choice == 'negamax':
            color = 1 if self.ai_symbol == 'O' else -1
            eval_score, move = negamax(self.game_state, depth=depth, color=color)
        else: 
            raise ValueError("Invalid Choice.")
        
        if move is not None:
            x, y = move
            self.game_state.board_state[x][y] = 1 if self.ai_symbol == 'O'else -1
            if self.ai_symbol == 'O':
                self.draw_circle(x, y)
            else:
                self.draw_cross(x, y)
            if self.is_game_over():
                self.display_winner()
                pygame.time.wait(5000)
                self.game_reset()
            else:self.change_turn()

        else:
            print("No moves left!")
        
        pygame.display.update()
        terminal = self.game_state.is_terminal()
        """ USE self.game_state.get_scores(terminal) HERE TO COMPUTE AND DISPLAY THE FINAL SCORES """



    def game_reset(self):
        self.draw_game()
        """
        YOUR CODE HERE TO RESET THE BOARD TO VALUE 0 FOR ALL CELLS AND CREATE A NEW GAME STATE WITH NEWLY INITIALIZED
        BOARD STATE
        """
        
        pygame.display.update()

    def play_game(self, mode = "player_vs_ai"):
        done = False
        clock = pygame.time.Clock()

        while not done:
            for event in pygame.event.get():  # User did something
                """
                YOUR CODE HERE TO CHECK IF THE USER CLICKED ON A GRID ITEM. EXIT THE GAME IF THE USER CLICKED EXIT
                """
                
                """
                YOUR CODE HERE TO HANDLE THE SITUATION IF THE GAME IS OVER. IF THE GAME IS OVER THEN DISPLAY THE SCORE,
                THE WINNER, AND POSSIBLY WAIT FOR THE USER TO CLEAR THE BOARD AND START THE GAME AGAIN (OR CLICK EXIT)
                """
                    
                """
                YOUR CODE HERE TO NOW CHECK WHAT TO DO IF THE GAME IS NOT OVER AND THE USER SELECTED A NON EMPTY CELL
                IF CLICKED A NON EMPTY CELL, THEN GET THE X,Y POSITION, SET ITS VALUE TO 1 (SELECTED BY HUMAN PLAYER),
                DRAW CROSS (OR NOUGHT DEPENDING ON WHICH SYMBOL YOU CHOSE FOR YOURSELF FROM THE gui) AND CALL YOUR 
                PLAY_AI FUNCTION TO LET THE AGENT PLAY AGAINST YOU
                """
                
                # if event.type == pygame.MOUSEBUTTONUP:
                    # Get the position
                    
                    # Change the x/y screen coordinates to grid coordinates
                    
                    # Check if the game is human vs human or human vs AI player from the GUI. 
                    # If it is human vs human then your opponent should have the value of the selected cell set to -1
                    # Then draw the symbol for your opponent in the selected cell
                    # Within this code portion, continue checking if the game has ended by using is_terminal function
                    
            # Update the screen with what was drawn.
            pygame.display.update()

        pygame.quit()

tictactoegame = RandomBoardTicTacToe()
"""
YOUR CODE HERE TO SELECT THE OPTIONS VIA THE GUI CALLED FROM THE ABOVE LINE
AFTER THE ABOVE LINE, THE USER SHOULD SELECT THE OPTIONS AND START THE GAME. 
YOUR FUNCTION PLAY_GAME SHOULD THEN BE CALLED WITH THE RIGHT OPTIONS AS SOON
AS THE USER STARTS THE GAME
"""
