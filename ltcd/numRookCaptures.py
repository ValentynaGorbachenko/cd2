'''
On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.
Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: 
In this example the rook is able to capture all the pawns.

Input: [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 0
Explanation: 
Bishops are blocking the rook to capture any pawn.

Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: 
The rook can capture the pawns at positions b5, d6 and f5.

'''
def numRookCaptures(board):
    count = 0
    for i, row in enumerate(board):
        if "R" in row:
            j = row.index("R")
            u, d, r, l = i, i, j, j
            
            
            print("i is ", i, " j is ", j)
            
            # up
            while u-1 != -1:
                print("u-1 != -1 ", u-1 != -1)
                if board[u-1][j] == ".":
                    u-=1
                elif board[u-1][j] == "B":
                    break
                elif board[u-1][j] == "p":
                    count+=1
                    break
            print("count after up ",count)
            # down
            
            while d+1 != len(board):
                print("d+1 != len(board) ", d+1 != len(board))
                if board[d+1][j] == ".":
                    d +=1
                elif board[d+1][j] == "B":
                    break
                elif board[d+1][j] == "p":
                    count+=1
                    break
            
            # left
            while l-1 != -1:
                print("l-1 != -1 ",l-1 != -1)
                if board[i][l-1] == ".":
                    l-=1
                elif board[i][l-1] == "B":
                    break
                elif board[i][l-1] == "p":
                    count+=1
                    break

            # right
            while r+1 != len(row):
                print("r+1 != len(row) ",r+1 != len(row))
                if board[i][r+1] == ".":
                    r+=1
                elif board[i][r+1] == "B":
                    break
                elif board[i][r+1] == "p":
                    count+=1
                    break
        
    print (count)
    return count

numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]])

'''
[
[".",".",".",".",".",".",".","."],
[".",".",".","p",".",".",".","."],
[".",".",".","R",".",".",".","p"],
[".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".","."],
[".",".",".","p",".",".",".","."],
[".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".","."]]


[
[".",".",".",".",".",".",".","."],
[".",".",".","p",".",".",".","."],
[".",".",".","B",".",".",".","."],
[".","p","B","R","p","B","p","."],
[".",".",".","p","p",".",".","."],
[".",".",".","B",".",".",".","."],
[".",".",".","p",".",".",".","."],
[".",".",".",".",".",".",".","."]]

'''


