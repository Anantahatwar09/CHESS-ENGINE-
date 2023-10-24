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
        self.white = True
        self.movelog = []

    def makemove(self, move):
        self.board[move.startrow][move.startcol] = "--"
        self.board[move.endrow][move.endcol] = move.pieceMoved
        self.movelog.append(move)
        self.white = not self.white

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

    def chessnotation(self):
        return self.rankfile(self.startcol, self.startrow) + self.rankfile(self.endcol, self.endrow)

    def rankfile(self, r, c):
        return self.colstofile[c] + self.rowstorank[r]

