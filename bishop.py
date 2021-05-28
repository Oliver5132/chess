import pygame
from color import Color
from constants import SQUARE_SIZE

class Bishop(object):
    def __init__(self, row, col, board):
        self.row = row
        self.col = col
        self.board = board
        self.side = self.board.chess_board[row][col][0]
        if self.side == 'w':
            self.opposite_side = 'b'
        elif self.side == 'b':
            self.opposite_side ='w'
        else:
            self.opposite_side = None
    
    def draw_valid_moves(self, screen, valid_moves):
        if self.board.chess_board[self.row][self.col][1] == 'B':
            for valid_move in valid_moves:
                pygame.draw.circle(screen, Color.YELLOW, (valid_move[1]* SQUARE_SIZE + SQUARE_SIZE//2, valid_move[0]* SQUARE_SIZE + SQUARE_SIZE//2), 15)


    def get_valid_moves(self):
        valid_moves = []
        self.get_right_diag(valid_moves)
        self.get_left_diag(valid_moves)

        print(valid_moves)
        return valid_moves

    def get_left_diag(self, valid_moves):
        row = self.row + 1
        col = self.col - 1
        while row < 8 and col > -1:
            if self.board.chess_board[row][col][0] == self.side:
                break
            elif self.board.chess_board[row][col] == '--':
                valid_moves.append([row, col])
            elif self.opposite_side is not None:
                if self.board.chess_board[row][col][0] == self.opposite_side:
                    valid_moves.append([row, col])
                    break
            row += 1
            col -= 1

        row = self.row - 1
        col = self.col + 1
        while row > -1 and col < 8:
            if self.board.chess_board[row][col][0] == self.side:
                break
            elif self.board.chess_board[row][col] == '--':
                valid_moves.append([row, col])
            elif self.opposite_side is not None:
                if self.board.chess_board[row][col][0] == self.opposite_side:
                    valid_moves.append([row, col])
                    break
            row -= 1
            col += 1

    def get_right_diag(self, valid_moves):
        row = self.row + 1
        col = self.col + 1
        while row < 8 and col < 8:
            if self.board.chess_board[row][col][0] == self.side:
                break
            elif self.board.chess_board[row][col] == "--":
                valid_moves.append([row, col])
            elif self.opposite_side is not None:
                if self.board.chess_board[row][col][0] == self.opposite_side:
                    valid_moves.append([row, col])
                    break
            row += 1
            col += 1

        row = self.row - 1
        col = self.col - 1
        while row > -1 and col > -1:
            if self.board.chess_board[row][col][0] == self.side:
                break
            elif self.board.chess_board[row][col] == "--":
                valid_moves.append([row, col])
            elif self.opposite_side is not None:
                if self.board.chess_board[row][col][0] == self.opposite_side:
                    valid_moves.append([row, col])
                    break
            row -= 1
            col -= 1
