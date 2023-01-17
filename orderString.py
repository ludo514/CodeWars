
def order(sentence):
    newSentence = sentence.split(" ")
    newSentence2 = []
    i = 0
    b = 1
    while i < len(newSentence):
        if str(b) in newSentence[i]:
            newSentence2.append(newSentence[i])
            newSentence.pop(i)
            b += 1
            i = 0
        else:
            i+=1
    return " ".join(newSentence2)

print(order("is2 Thi1s T4est 3a"))