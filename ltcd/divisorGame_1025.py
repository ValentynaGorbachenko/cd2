'''
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.

 

Example 1:

Input: 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
Example 2:

Input: 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
 

Note:

1 <= N <= 1000
'''

def helper(n):
    
    for x in range(n-1,0,-1):
        if n%x==0 and x%4 == 0:
            return 1
        elif n%x==0 and x%6 == 0:
            return 6
        elif n%x==0 and x%8==0:
            return 8
        elif n%x==0:
            return x
        else:
            return 1



def divisorGame(N):
    count = 0
    # if alice starts the game she will win if count%2==1
    # if N == 1 game is over
    print("type in divisorGame ", type(N), N)
    while N!=1:
        x = helper(N)
        N -= x
        count +=1

    return count%2 == 1

# this all comes to the point that the function should look like this

def divisorGameOpt(N):
    return N%2 == 0

# print(divisorGame(15))
# print(divisorGame(3))





