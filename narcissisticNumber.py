# res = [ int(x) for x in str(num)]

import math
def narcissistic( value ):
    resultat = 0
    valueTab = [ int(x) for x in str(value)]
    numberOfDigits = len(valueTab)
    for x in valueTab:
        resultat += math.pow(x, numberOfDigits)
    if resultat == value:
        return True
    else:
        return False
print(narcissistic(7))