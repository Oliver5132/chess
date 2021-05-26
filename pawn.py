class Pawn(object):
    def __init__(self, row , col , side, board) -> None:
        self.row = row
        self.col = col
        self.side = side
        self.board = board

    def get_valid_moves(self):
        valid_moves = []
        if self.side == "w":
            if self.board.chess_board[self.row - 1][self.col] == "--":
                valid_moves.append([self.row-1, self.col])
                if self.row == 6 and self.board.chess_board[self.row - 2][self.col] == "--":
                    valid_moves.append([self.row - 2, self.col])
            if self.board.chess_board[self.row - 1][self.col - 1][0] == 'b':
                valid_moves.append([self.row - 1, self.col - 1])
                print("READY TO CAPTURE")
            if self.board.chess_board[self.row - 1][self.col + 1][0] == 'b':
                valid_moves.append([self.row - 1, self.col + 1])

        elif self.side == "b":
            if self.board.chess_board[self.row + 1][self.col] == "--":
                valid_moves.append([self.row+1, self.col])
                if self.row == 1 and self.board.chess_board[self.row + 2][self.col] == "--":
                    valid_moves.append([self.row + 2,self.col])
            if self.board.chess_board[self.row + 1][self.col - 1][0] == 'w':
                valid_moves.append([self.row + 1, self.col - 1])
                print("READY TO CAPTURE")
            if self.board.chess_board[self.row + 1][self.col + 1][0] == 'w':
                valid_moves.append([self.row + 1, self.col + 1])
        
        print(valid_moves)
        return valid_moves