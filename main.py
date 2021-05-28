from bishop import Bishop
import pygame, sys
from board import Board
from screen import Screen
from pawn import Pawn
from rook import Rook

pygame.init()

win = Screen()
board = Board()

def main():
    run = True
    draw = False
    while run:
        board.draw_gamestate(win.screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                print(location)
                row, col = board.get_col_row(location)
                print(row, col)
                if board.whiteTomove and board.chess_board[row][col] in board.black_pieces and (not board.white_piece_selected):
                    print("WHITE TO MOVE")
                elif board.blackTomove and board.chess_board[row][col] in board.white_pieces and (not board.black_piece_selected):
                    if not board.black_piece_selected:
                        print("BLACK TO BE MOVED")
                else:
                    pawn = Pawn(row, col, board)
                    rook = Rook(row, col, board)
                    bishop = Bishop(row, col, board)
                    draw = True
                    board.touch_check(row, col, Pawn, Rook, Bishop)
        if draw:
            pawn.draw_valid_moves(win.screen, pawn.get_valid_moves())
            rook.draw_valid_moves(win.screen, rook.get_valid_moves())
            bishop.draw_valid_moves(win.screen, bishop.get_valid_moves())

        win.update()
        win.clock.tick(60)

main()
