
class Edge:
    def __init__(self, id, eType):
        self.id = id
        self.eType = eType # flat, inner, outter
    
    # Check if inner -> outter
    def isPossibleMatch(edge1, edge2)
    
    # Possibly given dictionary of matching edge id's
    # If id 3 matches 4, dic[3] = 4 and dic[4] = 3
    def matches(edge1, edge2)
  
class Piece:
    def __init__(self, id, picture, leftEdge, topEdge, rightEdge, bottomEdge):
        self.id = id
        self.picture = picture
        # Surrounding edges
        self.leftEdge = leftEdge
        self.topEdge = topEdge
        self.rightEdge = rightEdge        
        self.bottomEdge = bottomEdge
        # Final orientation
        self.orientation = 0 # 0, 90, 180, 270

    # Updates orientation clockwise, and shifts all edge obj assignements
    def rotate(self)

class Puzzle:
    def __init__(self, piecesList, board):
        # List of usable piaces
        self.piecesList = piecesList
        # 2-d matrix, initially empty
        self.board = board
    
    # Remove piece from piecesList, add to board
    def placePieceOnBoard(self, pid, r1, c1)
    
    # Remove piece from board, insert back into piecesList
    def removePieceFromBoard(self, r1, c1):

    # Move a piece on the board
    def movePiece(self, r1, c1, r2, c2)

    # If a piece is on the board, checks if matches the surrounding pieces
    # Checks if flat edge, if on edge of board
    # Returns False if not a match, or a piece is not in that position
    def matchesLeft(self)
    def matchesRight(self)
    def matchesTop(self)
    def matchesBottom(self)

    # For each piece in board, compares against surrounding pieces
    def isSolved(self)
