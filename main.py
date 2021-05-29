import pygame, sys
from board import Board
from screen import Screen
from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King

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
                    knight = Knight(row, col, board)
                    queen = Queen(row, col, board)
                    king = King(row,col, board)
                    draw = True
                    board.touch_check(row, col, Pawn, Rook, Bishop, Knight, Queen, King)
        if draw:
            pawn.draw_valid_moves(win.screen, pawn.get_valid_moves())
            rook.draw_valid_moves(win.screen, rook.get_valid_moves())
            bishop.draw_valid_moves(win.screen, bishop.get_valid_moves())
            knight.draw_valid_moves(win.screen, knight.get_valid_moves())
            queen.draw_valid_moves(win.screen, queen.get_valid_moves())
            king.draw_valid_moves(win.screen, king.get_valid_moves())

        if board.white_king_check():
            win.draw_win_screen('BLACK WON!')
            draw = False

        elif board.black_king_check():
            win.draw_win_screen('WHITE WON!')
            draw = False

        win.update()
        win.clock.tick(60)

main()