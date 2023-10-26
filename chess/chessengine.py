class gamestate():
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
        
        self.movefunction = {
            'p': self.getpawnmove,
            'r': self.getrookmove,
            'n': self.getknightmove,
            'b': self.getbishopmove,
            'q': self.getqueenmove,
            'k': self.getkingmove
        }

        self.white = True
        self.movelog = []

    def makemove(self, move):
        self.board[move.startrow][move.startcol] = "--"
        self.board[move.endrow][move.endcol] = move.pieceMoved
        self.movelog.append(move)
        self.white = not self.white
        
    def undomoves(self):
        if len(self.movelog) > 0:
            last_move = self.movelog.pop()
            self.board[last_move.startrow][last_move.startcol] = last_move.pieceMoved
            self.board[last_move.endrow][last_move.endcol] = last_move.pieceCaptured
            self.white = not self.white
            
            
    def getvalidmoves(self):
        return self.getallpossiblemoves() ## when there is no check
    
    
    def getallpossiblemoves(self):
        moves = []  # Initialize an empty list to store moves
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == 'w' and self.white) or (turn == 'b' and not self.white):
                    piece = self.board[r][c][1]
                    self.movefunction[piece](r,c,moves)
        return moves  # Return the list of moves
    
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
              
class move():
    ranktorow = {
        "1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0
    }
    rowstorank = {v: k for k, v in ranktorow.items()}

    filetocol = {
        "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7
    }
    colstofile = {v: k for k, v in filetocol.items()}

    def __init__(self, startsq, endsq, board):
        self.startrow = startsq[0]
        self.startcol = startsq[1]
        self.endrow = endsq[0]
        self.endcol = endsq[1]
        self.pieceMoved = board[self.startrow][self.startcol]
        self.pieceCaptured = board[self.endrow][self.endcol]
        self.moveid = self.startrow*1000 + self.startcol*100 + self.endrow*10 + self.endcol
        print(self.moveid)
        
    def __eq__(self,other):
        if isinstance(other,move):
            return self.moveid == other.moveid
        return False    
 
    def chessnotation(self):
        return self.rankfile(self.startcol, self.startrow) + self.rankfile(self.endcol, self.endrow)

    def rankfile(self, r, c):
        return self.colstofile[c] + self.rowstorank[r]

