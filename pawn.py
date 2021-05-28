import pygame
from constants import SQUARE_SIZE
from color import Color

class Pawn(object):
    def __init__(self, row , col, board) -> None:
        self.row = row
        self.col = col
        self.side = board.chess_board[row][col][0]
        self.board = board

    def draw_valid_moves(self, screen, valid_moves):
        if self.board.chess_board[self.row][self.col][1] == 'p':
            for valid_move in valid_moves:
                pygame.draw.circle(screen, Color.YELLOW, (valid_move[1]* SQUARE_SIZE + SQUARE_SIZE//2, valid_move[0]* SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def get_valid_moves(self):
        valid_moves = []
        if self.side == "w":
            if self.board.chess_board[self.row - 1][self.col] == "--":
                valid_moves.append([self.row-1, self.col])
                if self.row == 6 and self.board.chess_board[self.row - 2][self.col] == "--":
                    valid_moves.append([self.row - 2, self.col])
            if self.col - 1 >= 0:
                if self.board.chess_board[self.row - 1][self.col - 1][0] == 'b':
                    valid_moves.append([self.row - 1, self.col - 1])
            if self.col + 1 <= 7:
                if self.board.chess_board[self.row - 1][self.col + 1][0] == 'b':
                    valid_moves.append([self.row - 1, self.col + 1])

        elif self.side == "b":
            if self.board.chess_board[self.row + 1][self.col] == "--":
                valid_moves.append([self.row+1, self.col])
                if self.row == 1 and self.board.chess_board[self.row + 2][self.col] == "--":
                    valid_moves.append([self.row + 2,self.col])
            if self.col - 1 >= 0:
                if self.board.chess_board[self.row + 1][self.col - 1][0] == 'w':
                    valid_moves.append([self.row + 1, self.col - 1])
            if self.col + 1 <= 7:
                if self.board.chess_board[self.row + 1][self.col + 1][0] == 'w':
                    valid_moves.append([self.row + 1, self.col + 1])
        
        return valid_moves