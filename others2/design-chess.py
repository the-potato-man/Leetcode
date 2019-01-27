# http://k2code.blogspot.com/2014/03/design-chess-game-using-oo-principles.html

class Piece:
    def __init__(self, pieceType, color):
        self.pieceType = pieceType # None, Pawn, Rook, Knight, Bishop, Queen, King
        self.color = color # Black, White

class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Board:
    def __init__(self):
        self.sqaureset = [][]
        self.pieceset = [][]
    
    def clone()

class Move:
    def __init__(self, fromSquare, toSquare, pieceMoved, pieceCaptured, promotionType, algebraicNotion):
        self.fromSquare = None
        self.toSquare = None
        self.pieceMoved = None
        self.pieceCaptured = None
        self.promotionType = None
        self.algebraicNotion = None

class Game:
    def __init__(self, board, moveList, turnType, doublePawnPUsh, halfMoves, player1, player2, status):
        self.board = board
        self.moveList = moveList
        self.turnType = turnType
        self.doublePawnPUsh = doublePawnPush
        self.halfMoves = halfMoves

        self.player1 = player1
        self.player2 = player2
        self.status

    def canWhiteCastleA()
    def canWhiteCastleH()
    def canBlackCastleA()
    def canBlackCastleH()
    
    def createAndPlacePieces()
    def setPlayerTurn()

    def play():
        while self.status != 'Game Over':
            changeTurn() # called movePiece on Piece object


