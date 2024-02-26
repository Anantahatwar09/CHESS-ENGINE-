class ChessGameState:
    def __init__(self):
        self.board = [
            ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
        ]
        
        self.move_functions = {
            'p': self.get_pawn_moves,
            'r': self.get_rook_moves,
            'n': self.get_knight_moves,
            'b': self.get_bishop_moves,
            'q': self.get_queen_moves,
            'k': self.get_king_moves
        }

        self.is_white_turn = True
        self.move_log = []

    def make_move(self, move):
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.move_log.append(move)
        self.is_white_turn = not self.is_white_turn
        
    def undo_moves(self):
        if len(self.move_log) > 0:
            last_move = self.move_log.pop()
            self.board[last_move.start_row][last_move.start_col] = last_move.piece_moved
            self.board[last_move.end_row][last_move.end_col] = last_move.piece_captured
            self.is_white_turn = not self.is_white_turn
            
    def get_valid_moves(self):
        return self.get_all_possible_moves() ## when there is no check
    
    def get_all_possible_moves(self):
        moves = []  # Initialize an empty list to store moves
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                color = self.board[r][c][0]
                if (color == 'w' and self.is_white_turn) or (color == 'b' and not self.is_white_turn):
                    piece = self.board[r][c][1]
                    self.move_functions[piece](r, c, moves)
        return moves  
    
    def getpawnmove(self, r, c, moves):
        if self.white:
            # Check one square ahead
            if r > 0 and self.board[r - 1][c] == "--":
                moves.append(move((r, c), (r - 1, c), self.board))
                
                # Check two squares ahead from the starting position
                if r == 6 and self.board[r - 2][c] == "--":
                    moves.append(move((r, c), (r - 2, c), self.board))
            
            # Check for capturing moves to the left and right
            if r > 0 and c > 0 and self.board[r - 1][c - 1][0] == 'b':
                moves.append(move((r, c), (r - 1, c - 1), self.board))
            if r > 0 and c < 7 and self.board[r - 1][c + 1][0] == 'b':
                moves.append(move((r, c), (r - 1, c + 1), self.board))
        else:
            # Check one square ahead
            if r < 7 and self.board[r + 1][c] == "--":
                moves.append(move((r, c), (r + 1, c), self.board))
                
                # Check two squares ahead from the starting position
                if r == 1 and self.board[r + 2][c] == "--":
                    moves.append(move((r, c), (r + 2, c), self.board))
            
            # Check for capturing moves to the left and right
            if r < 7 and c > 0 and self.board[r + 1][c - 1][0] == 'w':
                moves.append(move((r, c), (r + 1, c - 1), self.board))
            if r < 7 and c < 7 and self.board[r + 1][c + 1][0] == 'w':
                moves.append(move((r, c), (r + 1, c + 1), self.board))                    
    
    def getrookmove(self, r, c, moves):
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        color = 'w' if self.white else 'b'

        for dr, dc in directions:
            for i in range(1, 8):
                row, col = r + dr * i, c + dc * i
                if 0 <= row < 8 and 0 <= col < 8:
                    if self.board[row][col][0] == color:
                        break  # Cannot go through your pieces
                    moves.append(move((r, c), (row, col), self.board))
                    if self.board[row][col][0] != '-':
                        break  # Capture opponent's piece
                else:
                    break  # Out of board bounds

    
    def getknightmove(self, r, c, moves):
        pass        
    
    def getbishopmove(self, r, c, moves):
        pass
    
    def getqueenmove(self, r, c, moves):
        pass                       
    
    def getkingmove(self, r, c, moves):
        pass    
              
class ChessMove:
    rank_to_row = {
        "1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0
    }
    row_to_rank = {v: k for k, v in rank_to_row.items()}

    file_to_col = {
        "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7
    }
    col_to_file = {v: k for k, v in file_to_col.items()}

    def __init__(self, start_sq, end_sq, board):
        self.start_row = start_sq[0]
        self.start_col = start_sq[1]
        self.end_row = end_sq[0]
        self.end_col = end_sq[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]
        self.move_id = self.start_row * 1000 + self.start_col * 100 + self.end_row * 10 + self.end_col
        print(self.move_id)
        
    def __eq__(self, other):
        if isinstance(other, ChessMove):
            return self.move_id == other.move_id
        return False    
 
    def chess_notation(self):
        return self.rank_file(self.start_col, self.start_row) + self.rank_file(self.end_col, self.end_row)

    def rank_file(self, r, c):
        return self.col_to_file[c] + self.row_to_rank[r]

