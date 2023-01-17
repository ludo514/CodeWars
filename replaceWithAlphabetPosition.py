import string
def alphabet_position(text):
    
    lowercase_alphabets=list(string.ascii_lowercase)
    list_number = []
    i = 0
    while i < len(text):
        if text[i].lower() in lowercase_alphabets:
            list_number.append(str(lowercase_alphabets.index(text[i].lower())+1))
        i+=1
    return " ".join(list_number)
print(alphabet_position("The sunset sets at twelve o' clock."))