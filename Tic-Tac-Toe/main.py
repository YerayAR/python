# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from game import *
from player import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RamdomComputerPlayer('O')

    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
