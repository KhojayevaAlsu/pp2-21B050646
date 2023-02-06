'''Write a program to solve a classic puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have? 
create function: solve(numheads, numlegs)'''

def solve(numheads, numlegs):
    rabbits = int((numlegs - numheads*2)/2)
    chickens = int(numheads - rabbits)
    return rabbits,chickens

    
numheads = 35
numlegs = 94
print(solve(numheads, numlegs))
