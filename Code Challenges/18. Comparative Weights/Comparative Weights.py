# Function that will return the fewest number of times you have to use a scale to find one ball with an outlier weight out 8 balls.
def scaleOfTruth():
    
    # Suppose (O) designates all balls. Repeat the steps below until you have identified the outlier ball
    # Step 1: Take half the balls and distribute them evenly over each side of the scale.
    # Step 2: Compare the weights:
        # Step 2a: If the scale is balanced, these balls (W) are all weighted evenly and the outlier is among the other balls (O). Continue to step 3a.
        # Step 2b: If the scale is unbalanced, one of the balls on either the left (L) or right (R) side of the scale is the outlier. Continue to step 3b.
    # Step 3
        # Step 3a: Take half of the (O) balls and distribute them evenly over the left (L) and right (R) side of the scale. Continue to step 2.
        # Step 3b: Take the balls from one side of the scale (L) and compare them to an equal number of the (W) balls. Continue to step 2.
    
    # The steps explain aboved will yield a result in a macimum number of iterations:
    steps = 0
    no_balls = 8
    while no_balls > 1:
        steps += 1
        no_balls /= 2
    return steps

# Function that will return the fewest number of times you have to use a scale to find one ball with an outlier weight out n balls.
def scaleOfTruthN(n):
    steps = 0
    while n > 1:    
        steps += 1
        n /= 2
    return steps

# Driver program to test above function(s)
print(scaleOfTruth())
print(scaleOfTruthN(8) == 3)

# This code was written by Tim Vlek