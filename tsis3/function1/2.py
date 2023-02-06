'''Read in a Fahrenheit temperature. 
Calculate and display the equivalent centigrade temperature. 
The following formula is used for the conversion: C = (5 / 9) * (F - 32)'''


def to_centigrade(fahr):
    return (5 / 9) * (fahr - 32)


fahr = float(input())
print(to_centigrade(fahr))
