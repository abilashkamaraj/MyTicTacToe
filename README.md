# MyTicTacToe
#Tic Tac Toe game using python and tkinter

##Open TicTacToe.py to view the source code
##Download TicTacToeApp folder and run the .exe file

* Two player game developed using python Tkinter library.
* When the game starts, one among the two players will be chosen randomly and that player will have the privilege to choose the marker first and goes first into the game.
* After choosing the markers for the players the main board will be displayed which is a 3*3 grid of buttons. The underlying data structure used to represent the board is a python list of 10 elements. The list initially has 10 space characters. The element at index x corresponds to the button x in the board.
* When the player clicks a button x the element at index x in the list will be checked if it is a space or not. If it is a space then the marker corresponding to the player will be placed on the button and element at index x will be set to the marker.
* After the marker is placed there will be a win check corresponding to the player’s marker, if that marker has won then the result will be displayed and the game will ask for a replay.
* If the marker corresponding to the player has not won, then there will be a draw check and if it is a draw then the result will be displayed and the game will ask for a replay.
* If there is no draw, then the turn goes to next player and the process continues.

