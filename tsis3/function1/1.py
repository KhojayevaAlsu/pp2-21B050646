'''
A recipe you are reading states how many grams you need for the ingredient. 
Unfortunately, your store only sells items in ounces. 
Create a function to convert grams to ounces. ounces = 28.3495231 * grams
'''
def to_ounces(gramms):
    return gramms*28.3495231

    
gramms = float(input())
print(to_ounces(gramms))