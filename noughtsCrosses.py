# Author: Jovanny Gochez
# Course: CSIS 126E
# Date: May 15, 2021
# Assignment: Portfolio Project

import numpy as np


class TTT:
    """
    Class provides functionality and implementation for tic-tac-toe
    game. Methods will first render and display the game board. They
    will then check for winner before any move. When no winner is found
    the user will make a move, move will be checked for legality, if
    valid, the move is made and the next player moves. This process
    repeats until a winner is found and the user will be asked if they
    would like to reload the game, if so, the method that reloads the
    game will empty the board and the game initializes as before.
    """

    def __init__(self) -> None:
        """Initiate empty ttt board and data members"""

        self.BOARD = np.empty((3, 3), dtype=str)
        self.BOARD[:, :] = ' '
        self.board_row = None
        self.board_column = None

    def render_board(self) -> None:
        """Print current state of board"""

        print(self.BOARD)

    def restart_game(self) -> None:
        """Once game is finished, function empties ttt board"""

        self.BOARD[:, :] = ' '

    def game_title(self) -> None:
        """Function prints title and sample board once when game is initiated"""

        print("--------------------------------")
        print("          TIC TAC TOE!          ")
        print("--------------------------------")
        print(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        print("-----------------------------------------")
        print("Integers on board represent the position!")
        print("-----------------------------------------")

    def player_move(self, square: int, player: str) -> None:
        """Function takes in square number and inputs player into position"""
        self.board_row = (square - 1) // 3
        self.board_column = (square - 1) % 3
        for row in self.BOARD:
            for cell in row:
                if self.BOARD[self.board_row, self.board_column] == ' ':
                    self.BOARD[self.board_row, self.board_column] = player

    def check_for_winner(self, player: str) -> bool:
        """check all conditions to find winner"""

        # Check and print if all values in any column matches either player
        if np.any(np.all(self.BOARD == player, axis=1)):
            print("----------------")
            print(f"Player '{player}' wins!")
            return False
        # Check and print if all values in any row matches either player
        elif np.any(np.all(self.BOARD == player, axis=0)):
            print("----------------")
            print(f"Player '{player}' wins!")
            return False
        # Check and print if all values in first diagonal row matches either player
        elif np.all(self.BOARD.diagonal() == player):
            print("----------------")
            print(f"Player '{player}' wins!")
            return False
        # Check and print if all values in second diagonal row matches either player
        elif np.all(np.flipud(self.BOARD).diagonal() == player):
            print("----------------")
            print(f"Player '{player}' wins!")
            return False
        # If no player has won continue game by returning bool value: True
        else:
            print('Next Player:')
            return True


def main():
    # Game is initiated here
    game_obj = TTT()
    game_obj.game_title()
    game_in_session = True
    current_player = 'O'

    while game_in_session == True:
        # Boolean to keep game in session
        game_obj.render_board()
        PLAYER_MOVE = int(input("Current Player Pick Position: "))
        # Validate player input
        if 1 <= PLAYER_MOVE <= 9:
            # Keep track of player
            if current_player == 'O':
                current_player = 'X'
            else:
                current_player = 'O'
            # Player move is made and inquiry for winner occurs here
            game_obj.player_move(PLAYER_MOVE, current_player)
            game_in_session = game_obj.check_for_winner(current_player)

            # If a winner is found opportunity to restart game or quit occurs
            if game_in_session == False:
                game_obj.render_board()
                print('GAME OVER!!!')
                RELOAD_CHOICE = input("Restart Game? y/n: ").upper()
                if RELOAD_CHOICE == 'Y':
                    game_obj.restart_game()
                    game_in_session = True
                elif RELOAD_CHOICE == 'N':
                    game_in_session = False

    print('\nTHANK YOU FOR PLAYING!!!\n')


if __name__ == '__main__':
    main()
