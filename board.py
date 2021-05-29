import pygame
from color import Color
from constants import ROWS, COLS, SQUARE_SIZE

class Board(object):
    # LISTS
    chess_board = [
        ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
        ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
        ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'] 
    ]
    def __init__(self):
        # DICT for storing pieces with the image
        self.images = {}

        self.pieces = ['wp', 'wR', 'wN','wB' ,'wK', 'wQ', 'bp', 'bB' ,'bR', 'bN', 'bK', 'bQ']
        self.white_pieces = self.pieces[0:6]
        self.black_pieces = self.pieces[6:]
        self.square_pos = []
        self.empty_square = []
        self.current_piece = []
        self.current_square = []
        self.black_piece = []
        self.white_piece = []

        # BOOLS
        self.piece_selected = False
        self.white_piece_selected = False
        self.black_piece_selected = False
        self.square_selected = False
        self.whiteTomove = True
        self.blackTomove = False

        # Initiating the methods right when the object gets created.
        self.load_images()

    @staticmethod
    def draw_board(screen):
        colors = [Color.BROWN, Color.WHITE]
        for row in range(ROWS):
            for col in range(COLS):
                color = colors[((row+col)% 2)]
                pygame.draw.rect(screen, color, pygame.Rect(row* SQUARE_SIZE, col* SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
     
    def load_images(self):
        for piece in self.pieces:
            self.images[piece] = pygame.transform.scale(pygame.image.load("images/" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))

    def draw_pieces(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                self.square_pos.append([row*SQUARE_SIZE, col*SQUARE_SIZE])
                piece = self.chess_board[row][col]
                if piece != "--":
                    screen.blit(self.images[piece], pygame.Rect(col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_gamestate(self, screen):
        self.draw_board(screen)
        self.draw_pieces(screen)

    def move(self, index: list, location: list, Pawn, Rook, Bishop, Knight, Queen, King):
        if self.chess_board[index[0]][index[1]][1] == 'p':
            pawn = Pawn(index[0], index[1], self)
            valid_moves = pawn.get_valid_moves()
            for valid_move in valid_moves:
                if valid_move == location:
                    piece = self.chess_board[index[0]][index[1]]
                    self.chess_board[location[0]][location[1]] = piece
                    self.chess_board[index[0]][index[1]] = "--"
        elif self.chess_board[index[0]][index[1]][1] == 'R':
            rook = Rook(index[0], index[1], self)
            valid_moves = rook.get_valid_moves()
            for valid_move in valid_moves:
                if valid_move == location:
                    piece = self.chess_board[index[0]][index[1]]
                    self.chess_board[location[0]][location[1]] = piece
                    self.chess_board[index[0]][index[1]] = "--"
        elif self.chess_board[index[0]][index[1]][1] == 'B':
            bishop = Bishop(index[0], index[1], self)
            valid_moves = bishop.get_valid_moves()
            for valid_move in valid_moves:
                if valid_move == location:
                    piece = self.chess_board[index[0]][index[1]]
                    self.chess_board[location[0]][location[1]] = piece
                    self.chess_board[index[0]][index[1]] = "--"
        elif self.chess_board[index[0]][index[1]][1] == 'N':
            knight = Knight(index[0], index[1], self)
            valid_moves = knight.get_valid_moves()
            for valid_move in valid_moves:
                if valid_move == location:
                    piece = self.chess_board[index[0]][index[1]]
                    self.chess_board[location[0]][location[1]] = piece
                    self.chess_board[index[0]][index[1]] = "--"
        elif self.chess_board[index[0]][index[1]][1] == 'Q':
            queen = Queen(index[0], index[1], self)
            valid_moves = queen.get_valid_moves()
            for valid_move in valid_moves:
                if valid_move == location:
                    piece = self.chess_board[index[0]][index[1]]
                    self.chess_board[location[0]][location[1]] = piece
                    self.chess_board[index[0]][index[1]] = "--"
        elif self.chess_board[index[0]][index[1]] == 'K':
            king = King(index[0], index[1], self)
            valid_moves = king.get_valid_moves()
            for valid_move in valid_moves:
                if valid_move == location:
                    piece = self.chess_board[index[0]][index[1]]
                    self.chess_board[location[0]][location[1]] = piece
                    self.chess_board[index[0]][index[1]] = "--"
        else:
            piece = self.chess_board[index[0]][index[1]]
            self.chess_board[location[0]][location[1]] = piece
            self.chess_board[index[0]][index[1]] = "--"
            print("move working")

    @staticmethod
    def get_col_row(pos):
        col = pos[0] // SQUARE_SIZE
        row = pos[1] // SQUARE_SIZE

        return [row, col]

    # TO DEBUG
    def touch_check(self, row, col, Piece, Rook, Bishop, Knight, Queen, King):
        if self.chess_board[row][col] in self.white_pieces:
            self.white_piece_selected = True
            self.white_piece = [row, col]

        elif self.chess_board[row][col] in self.black_pieces:
            self.black_piece_selected = True
            self.black_piece = [row, col]
        elif self.chess_board[row][col] == "--":
            if self.whiteTomove and self.white_piece_selected:
                self.square_selected = True
                self.current_square = [row, col]
            elif self.blackTomove and self.black_piece_selected:
                self.square_selected = True
                self.current_square = [row, col]
        if self.whiteTomove and self.black_piece_selected and self.white_piece_selected:
            if not self.square_selected:
                self.move(self.white_piece, self.black_piece, Piece, Rook, Bishop, Knight, Queen, King)
                self.change_turn()
                self.white_piece_selected = False
                self.black_piece_selected = False
        elif self.blackTomove and self.white_piece_selected and self.white_piece_selected:
            if not self.square_selected:
                self.move(self.black_piece, self.white_piece, Piece, Rook, Bishop, Knight, Queen, King)
                self.change_turn()
                self.white_piece_selected = False
                self.black_piece_selected = False

        elif self.whiteTomove and self.white_piece_selected:
            if self.square_selected:
                self.move(self.white_piece, self.current_square, Piece, Rook, Bishop, Knight, Queen, King)
                self.change_turn()
                self.white_piece_selected = False
                self.square_selected = False
        elif self.blackTomove and self.black_piece_selected:
            if self.square_selected:
                self.move(self.black_piece, self.current_square, Piece, Rook, Bishop, Knight, Queen, King)
                self.change_turn()
                self.black_piece_selected = False
                self.black_piece_selected = False
                self.square_selected = False

    def change_turn(self):
        if self.whiteTomove:
            self.blackTomove = True
            self.whiteTomove = False
        elif self.blackTomove:
            self.whiteTomove = True
            self.blackTomove = False