#!/usr/bin/python
board = []
for i in range(0,5):
    board.append(["O"]*5)

print board

def print_board(x):
    for i in x:
        print " ".join(i)

print_board(board)
