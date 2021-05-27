import pygame
from color import Color
from constants import SQUARE_SIZE

class Rook(object):
    def __init__(self, row, col, board):
        self.row = row
        self.col = col
        self.board = board
        self.side = self.board.chess_board[row][col][0]
        print(self.side)
        if self.side == "w":
            self.opposite_side = "b"
        else:
            self.opposite_side = "w"

    def draw_valid_moves(self, screen, valid_moves):
        if self.board.chess_board[self.row][self.col][1] == 'R':
            for valid_move in valid_moves:
                pygame.draw.circle(screen, Color.YELLOW, (valid_move[1]* SQUARE_SIZE + SQUARE_SIZE//2, valid_move[0]* SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def get_valid_moves(self):
        valid_moves = []
        for row in range(self.row + 1, 8):
            if self.board.chess_board[row][self.col] == self.side:
                break
            elif self.board.chess_board[row][self.col][0] == self.opposite_side:
                valid_moves.append([row, self.col])
                break
            elif self.board.chess_board[row][self.col] == "--":
                valid_moves.append([row, self.col])
        
        for row in range(self.row, -1, -1):
            if self.board.chess_board[row][self.col] == self.side:
                break
            elif self.board.chess_board[row][self.col][0] == self.opposite_side:
                valid_moves.append([row, self.col])
                break
            elif self.board.chess_board[row][self.col] == "--":
                valid_moves.append([row, self.col])

        for col in range(self.col, 8):
            if self.board.chess_board[self.row][col] == self.side:
                break
            elif self.board.chess_board[self.row][col][0] == self.opposite_side:
                valid_moves.append([self.row, col])
                break
            elif self.board.chess_board[self.row][col] == "--":
                valid_moves.append([self.row, col])
        
        for col in range(self.col, -1, -1):
            if self.board.chess_board[row][self.col][0] == self.side:
                break
            elif self.board.chess_board[self.row][self.col][0] == self.opposite_side:
                valid_moves.append([self.row, self.col])
                break
            elif self.board.chess_board[self.row][col] == "--":
                valid_moves.append([self.row, col])

        # print(valid_moves)
        return valid_moves