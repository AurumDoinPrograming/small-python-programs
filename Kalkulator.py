print('''
Dette er en kalkulator. 
Først vil den spørre deg om et tall.
Så kan du velge regneart, da har du fire allternativer gange (G) dele (D) pluss (P) minus (M).
Du kan gjøre så mange ganger du vil.
Trykk enter når du er ferdig med å bruke kalkulatoren.
''')

def adder(tall):
    tallto = float(input('Andre tall\n'))
    return(float(tall) + tallto )
    
def subtraher(tall):
    tallto = float(input('Andre tall\n'))
    return(float(tall) - tallto )

def multipliser(tall):
    tallto = float(input('Andre tall\n'))
    return(float(tall) * tallto)

def divider(tall):
    tallto = float(input('Andre tall\n'))
    return(float(tall) / tallto )

regneart = 123
sluttsum = input('Skiv inn et tall\n')
while regneart != "":
    regneart = input('Velg regneart\n')
    if regneart.upper() == "P":
        sluttsum = adder(sluttsum)
    if regneart.upper() == "M":
        sluttsum = subtraher(sluttsum)
    if regneart.upper() == "G":
        sluttsum = multipliser(sluttsum)
    if regneart.upper() == "D":
        sluttsum = divider(sluttsum)
    print("Ferdig! Svaret er:", sluttsum)
