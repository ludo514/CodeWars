import math


symbol = {
    1:'I',
    5:'V',
    10:'X',
    50:'L',
    100:'C',
    500:'D',
    1000:'M'
}

def closet_value(n, keys):
    if n in keys:
        return n
    else:
        for i in keys:
            resultat = n - i
            if resultat == 1 or resultat == -1:
                return i
            elif resultat == 2 or resultat == -2:
                return i

def solution(n):
    number_of_digit = len(str(abs(n)))
    keys_symbol = [key for key, val in symbol.items()]
    digit_to_str = str(n)
    i = 0
    roman_number = ""
    while i < n:
        #number = int(digit_to_str[0]) * 100
        close_value = closet_value(int(n), keys_symbol)
        if n < close_value:
            if close_value - n != 2:
                roman_number += symbol[close_value - n]
                n += 1
            else:
                roman_number += symbol[close_value - 5]
                n -= 5
        roman_number += symbol[closet_value(int(n), keys_symbol)]
        n -= closet_value(int(n), keys_symbol)
        n = n.__abs__()
    return roman_number
    #print(str(n).split(" "))
print(solution(4))