#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
import numpy as np


class TicTacToeBoard(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        parent.geometry("300x350")
        self.num = 1
        self.current_p = [0, 0]  # current index of 'p'
        self.current_c = [1, 1]  # current index of 'c'
        self.board = [[' ', ' ', ' '], [' ', 'x', ' '], [' ', ' ', ' ']]
        self.board_state = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])  # 0 is empty, 1 is unavailable, 2 is temply unavaliable
        self.start_game()

    def start_game(self):
        self.b = {}  # nine buttons
        self.b["00"] = Button(root, bitmap="info", text=' ', width=70, height=85, compound=LEFT, command=lambda: self.drawxo(0, 0))
        self.b["01"] = Button(root, bitmap="info", text=' ', width=70, height=85, compound=LEFT, command=lambda: self.drawxo(0, 1))
        self.b["02"] = Button(root, bitmap="info", text=' ', width=70, height=85, compound=LEFT, command=lambda: self.drawxo(0, 2))
        self.b["10"] = Button(root, bitmap="info", text=' ', width=70, height=85, compound=LEFT, command=lambda: self.drawxo(1, 0))
        self.b["11"] = Button(root, bitmap="info", text=' ', width=70, height=85, compound=LEFT, command=lambda: self.drawxo(1, 1))
        self.b["12"] = Button(root, bitmap="info", text=' ', width=70, height=85, compound=LEFT, command=lambda: self.drawxo(1, 2))
        self.b["20"] = Button(root, bitmap="info", text=' ', width=70, height=85, compound=LEFT, command=lambda: self.drawxo(2, 0))
        self.b["21"] = Button(root, bitmap="info", text=' ', width=70, height=85, compound=LEFT, command=lambda: self.drawxo(2, 1))
        self.b["22"] = Button(root, bitmap="info", text=' ', width=70, height=85, compound=LEFT, command=lambda: self.drawxo(2, 2))
        self.b["00"].place(x=0, y=0)
        self.b["01"].place(x=100, y=0)
        self.b["02"].place(x=200, y=0)
        self.b["10"].place(x=0, y=100)
        self.b["11"].place(x=100, y=100)
        self.b["12"].place(x=200, y=100)
        self.b["20"].place(x=0, y=200)
        self.b["21"].place(x=100, y=200)
        self.b["22"].place(x=200, y=200)
        self.b["11"].config(text='X', font=("Courier", "50"))  # initial center button
        self.label3 = Label(root, text='Your turn!')  # bottom label
        self.label3.place(x=80, y=314)
        closebutton4 = Button(root, text='exit', command=root.destroy)  # quit button
        closebutton4.place(x=250, y=310)
        self.won = 0
        while self.won == 0 and self.num < 9:
            root.update()
        if self.won != 1:
            self.label3.config(text='CAT\'s GAME')  # tie
        else:
            self.label3.config(text='I WIN!')  # computer win

    def find_clockwise(self, x, y):
        if x - 1 > -1 and self.board[x - 1][y] == ' ':  # N
            if self.board_state[x - 1][y] != 2:
                return x-1, y
        if y + 1 < 3 and self.board[x][y + 1] == ' ':  # E
            if self.board_state[x][y + 1] != 2:
                return x, y + 1
        if x + 1 < 3 and self.board[x + 1][y] == ' ':  # S
            if self.board_state[x + 1][y] != 2:
                return x + 1, y
        if y - 1 > -1 and self.board[x][y - 1] == ' ':  # W
            if self.board_state[x][y - 1] != 2:
                return x, y - 1
        try:
            index = np.argwhere(self.board_state == 0)  # find the rest 0 in self.board_state, if any
            x, y = index[0][0], index[0][1]
            return x, y
        except:
            index = np.argwhere(self.board_state == 2)
            x, y = index[0][0], index[0][1]
            return x, y

    def drawxo(self, x, y):  # change the button to show X or O
        if self.won == 0:
            temp = str(x) + str(y)
            if self.board[x][y] == ' ' and self.num < 9:
                self.b[temp].config(text='O', font=("Courier","50"))  # change the button to show 'o'
                self.board[x][y] = 'o'
                self.board_state[x][y] = 1  # this position is occupied
                if self.board_state[2 - x][2 - y] == 0:  # change the oppisite position state
                    self.board_state[2 - x][2 - y] = 2  # opposite is temply unavaliable
                # set the computer's next chesspiece
                # Use the algorithm
                self.current_p[0] = x
                self.current_p[1] = y
                if self.num == 1:  # first move
                    x, y = self.find_clockwise(self.current_p[0], self.current_p[1])  # find the position of 'c'
                    self.b[str(x) + str(y)].config(text='X', font=("Courier", "50"))  # change the button to show 'X'
                    self.current_c[0],self.current_c[1] = x, y  # save the position of 'c'
                    self.board[x][y] = 'x'
                    self.board_state[x][y] = 1  # change the state
                    self.num += 2
                else:  # opposite is not p
                    if self.board[2 - self.current_c[0]][2 - self.current_c[1]] == ' ':  # computer win!
                        self.b[str(2 - self.current_c[0]) + str(2 - self.current_c[1])].config(text='X', font=("Courier","50"))  # change the button to show 'X'
                        self.board[2 - self.current_c[0]][2 - self.current_c[1]] = 'x'
                        self.board_state[2 - self.current_c[0]][2 - self.current_c[1]] = 1
                        self.won = 1  # don not change the button any more
                        self.num += 2
                    else:
                        x, y = self.find_clockwise(2 - self.current_c[0], 2 - self.current_c[1])
                        self.b[str(x) + str(y)].config(text='X', font=("Courier", "50"))
                        self.current_c[0],self.current_c[1] = x, y
                        self.board[x][y] = 'x'
                        self.board_state[x][y] = 1
                        self.num += 2

    def close(self):  # quit
        root.destroy()


root = Tk()  # main window
root.title("Tic Tac Toe")
board = TicTacToeBoard(root)
board.grid()
root.mainloop()