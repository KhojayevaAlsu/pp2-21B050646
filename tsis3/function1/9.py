'''Write a function that computes the volume of a sphere given its radius'''

def volume(r):
    V = 4/3 * (3.14 * r**3)
    return float(V)

r = float(input())
print(volume(r))