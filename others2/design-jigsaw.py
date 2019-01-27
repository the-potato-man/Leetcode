# http://k2code.blogspot.com/2014/03/implement-jigsaw-puzzle.html

class Edge:
    def __init__(self, id, edgeType, parentPiece):
        self.id = id
        self.edgeType = edgeType # flat, inner, outter
        self.parentPiece = parentPiece
  
    def match(edge1, edge2)
  
class Piece:
    def __init__(self, id, leftEdge, topEdge, rightEdge, bottomEdge):
        self.id = id
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
    def __init__(self, pieces, solution):
        # 2-d matrix, randomly populated
        self.pieces = pieces
        # 2-d matrix, initially empty
        self.solution = solution

    '''
    Iterate through all edges in given pieces, adding to inners, outers, flats
    Add non-flat edges of corner pieces to exposed edges
    Add one corner piece to any corner in self.solution
    '''
    self.inners = []
    self.outers = []
    self.flats = []
    self.exposedEdges = []
    def sort()
    
    def solve():
        for edge1 in self.exposedEdges:
            if edge1.type = 'inner':
                for edge2 in self.outers:
                    if edge1.fitsWith(edge2):
                        # remove edge1 from self.exposedEdges
                        # rotate and add piece, associated with edge2, to solution
                        # check which edges of edge2 are exposed and add to self.exposedEdges
                # Do the same thing, swapping inner and outer

    # For User actions

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
