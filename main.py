import pygame, sys
from board import Board
from screen import Screen

pygame.init()

win = Screen()
board = Board()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                row, col = board.get_col_row(location)
                print(row, col)
                if board.whiteTomove and board.chess_board[row][col] in board.black_pieces and (not board.white_piece_selected):
                    print("WHITE TO MOVE")
                elif board.blackTomove and board.chess_board[row][col] in board.white_pieces and (not board.black_piece_selected):
                    if not board.black_piece_selected:
                        print("BLACK TO BE MOVED")
                else:
                    board.touch_check(row, col)
        board.draw_gamestate(win.screen)
        win.update()
        win.clock.tick(60)

main()
