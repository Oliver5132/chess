import pygame
from color import Color
from constants import SQUARE_SIZE

class King(object):
    def __init__(self, row, col, board):
        self.row = row
        self.col = col
        self.board = board
        self.side = self.board.chess_board[0]
        if self.side == 'w':
            self.opposite_side = 'b'
        elif self.side == 'b':
            self.opposite_side = 'w'
        else:
            self.opposite_side = None

    def draw_valid_moves(self, screen, valid_moves):
        for valid_move in valid_moves:
            if self.board.chess_board[self.row][self.col][1] == 'K':
                for valid_move in valid_moves:
                    pygame.draw.circle(screen, Color.YELLOW, (valid_move[1]* SQUARE_SIZE + SQUARE_SIZE//2, valid_move[0]* SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def get_valid_moves(self):
        valid_moves = []
        if self.row + 1 < 8:
            if self.board.chess_board[self.row + 1][self.col] == '--' or self.board.chess_board[self.row + 1][self.col][0] == self.opposite_side:
                valid_moves.append([self.row + 1, self.col])
        if self.row - 1 >= 0:
            if self.board.chess_board[self.row - 1][self.col] == '--' or self.board.chess_board[self.row - 1][self.col][0] == self.opposite_side:
                valid_moves.append([self.row - 1, self.col])
        if self.col + 1 < 8:
            if self.board.chess_board[self.row][self.col + 1] == '--' or self.board.chess_board[self.row][self.col + 1][0] == self.opposite_side: 
                valid_moves.append([self.row, self.col + 1])
        if self.col - 1 >= 0:
            if self.board.chess_board[self.row][self.col - 1] == '--' or self.board.chess_board[self.row][self.col - 1][0] == self.opposite_side:
                valid_moves.append([self.row, self.col - 1])
        if self.row + 1 < 8 and self.col + 1 < 8:
            if self.board.chess_board[self.row + 1][self.col + 1] == '--' or self.board.chess_board[self.row + 1][self.col + 1] == self.opposite_side:
                valid_moves.append([self.row + 1, self.col + 1])
        if self.row - 1 >= 0 and self.col - 1 >= 0:
            if self.board.chess_board[self.row - 1][self.col - 1] == '--' or self.board.chess_board[self.row - 1][self.col - 1] == self.opposite_side:
                valid_moves.append([self.row - 1, self.col - 1])
        if self.row - 1 >= 0 and self.col + 1 < 8:
            if self.board.chess_board[self.row - 1][self.col + 1] == '--' or self.board.chess_board[self.row - 1][self.col + 1] == self.opposite_side:
                valid_moves.append([self.row - 1, self.col + 1])
        if self.row + 1 < 8 and self.col - 1 >= 0:
            if self.board.chess_board[self.row + 1][self.col - 1] == '--' or self.board.chess_board[self.row + 1][self.col - 1] == self.opposite_side:
                valid_moves.append([self.row + 1, self.col - 1])

        return valid_moves