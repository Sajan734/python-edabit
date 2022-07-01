# In cricket, an over consists of six deliveries a bowler bowls from one end. Create a function that takes the number of balls bowled by a bowler and calculates the number of overs and balls bowled by him/her. Return the value as a float, in the format overs.balls.

def total_overs(balls):
    overs, balls = divmod(balls, 6)
    ballsFloat = float(balls/10)
    print(overs + ballsFloat)

total_overs(5)