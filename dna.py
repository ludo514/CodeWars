def DNA_strand(dna):
    dnaChange = ""
    for x in dna:
        if x == 'A':
            dnaChange += 'T'
        elif x == 'T':
            dnaChange += 'A'
        elif x == 'C':
            dnaChange += 'G'
        elif x == 'G':
            dnaChange += 'C'
    return dnaChange

print(DNA_strand("ATTGC"))