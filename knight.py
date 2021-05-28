import pygame
from constants import SQUARE_SIZE
from color import Color

class Knight(object):
    def __init__(self, row, col, board):
        self.row = row
        self.col = col
        self.board = board
        self.side = self.board.chess_board[row][col][0]
        if self.side == 'w':
            self.oppposite_side = 'b'
        elif self.side == 'b':
            self.oppposite_side = 'w'
        else:
            self.oppposite_side = None
    
    def draw_valid_moves(self, screen, valid_moves):
        if self.board.chess_board[self.row][self.col][1] == 'N':
            for valid_move in valid_moves:
                pygame.draw.circle(screen, Color.YELLOW, (valid_move[1]* SQUARE_SIZE + SQUARE_SIZE//2, valid_move[0]* SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def get_valid_moves(self):
        valid_moves = []
        self.forward_check(valid_moves)
        self.backward_check(valid_moves)
        self.right_check(valid_moves)
        self.left_check(valid_moves)

        return valid_moves

    def left_check(self, valid_moves):
        if self.row - 2 >= 0 and self.col + 1 < 8:
            if self.board.chess_board[self.row - 2][self.col + 1] == '--' or self.board.chess_board[self.row - 2][self.col + 1][0] == self.oppposite_side:
                valid_moves.append([self.row - 2, self.col + 1])
        if self.row + 1 < 8 and self.col - 2:
            if self.board.chess_board[self.row + 1][self.col - 2] == '--' or self.board.chess_board[self.row + 1][self.col - 2][0] == self.oppposite_side:
                valid_moves.append([self.row + 1, self.col - 2])
            
    def right_check(self, valid_moves):
        if self.row + 2 < 8 and self.col - 1 >= 0:
            if self.board.chess_board[self.row + 2][self.col - 1] == '--' or self.board.chess_board[self.row + 2][self.col - 1][0] == self.oppposite_side:
                valid_moves.append([self.row + 2, self.col - 1])
        if self.row - 1 >= 0 and self.col + 2 < 8:
            if self.board.chess_board[self.row - 1][self.col + 2] == '--' or self.board.chess_board[self.row - 1][self.col + 2][0] == self.oppposite_side:
                valid_moves.append([self.row - 1, self.col + 2])

    def backward_check(self, valid_moves):
        if self.row - 2 >= 0 and self.col - 1 >= 0:
            if self.board.chess_board[self.row - 2][self.col - 1] == '--' or self.board.chess_board[self.row - 2][self.col - 1][0] == self.oppposite_side:
                valid_moves.append([self.row - 2, self.col - 1])
        if self.row - 1 >= 0 and self.col - 2 >= 0:
            if self.board.chess_board[self.row - 1][self.col - 2] == '--' or self.board.chess_board[self.row - 1][self.col - 2][0] == self.oppposite_side:
                valid_moves.append([self.row - 1, self.col - 2])
    def forward_check(self, valid_moves):
        if self.row + 2 < 8 and self.col + 1 < 8:
            if self.board.chess_board[self.row + 2][self.col + 1] == '--' or self.board.chess_board[self.row + 2][self.col + 1][0] == self.oppposite_side:
                valid_moves.append([self.row + 2, self.col + 1])
        if self.row + 1 < 8 and self.col + 2 < 8:
            if self.board.chess_board[self.row + 1][self.col + 2] == '--' or self.board.chess_board[self.row + 1][self.col + 2][0] == self.oppposite_side:
                valid_moves.append([self.row + 1, self.col + 2])

