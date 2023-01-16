import time
 
def print_hangman():
    global HangmanDrawing
    global antall_feil
    HangmanDrawing = ['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
     +---+
     O   |
     |   |
         |
        ===''', '''
     +---+
     O   |
    /|   |
         |
        ===''', '''
     +---+
     O   |
    /|\  |
         |
        ===''', '''
     +---+
     O   |
    /|\  |
    /    |
        ===''', '''
     +---+
     O   |
    /|\  |
    / \  |
        ===''']
    print(HangmanDrawing[antall_feil])
    print(sjultord)
 
def sjekk_bokstav():
    global bokstav
    global gjett
    global sjultord
 
    if gjett == bokstav:
        ny_bokstav = gjett
    elif bokstav in alfabet:
        ny_bokstav = "_"
 
    return ny_bokstav
    
 
sjultord = ""
alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ!"
lite_alfabet = "abcdefghijklmnopqrstuvwxyzæøå!"
ord = "JONAS SUGER I HANGMAN!"
antall_feil = 0
 
for bokstav in ord:
    if bokstav in alfabet:
        sjultord = sjultord + "_ "
 
while True:
    print_hangman()
    if antall_feil > int(len(HangmanDrawing) - 2):
        print("Du tapte")
        break
 
    gjett = input("\nGjett en bokstav\n")
 
    if not len(gjett) == 1:
        print("\nBare gjett EN bokstav\n")
        time.sleep(1)
        continue
 
    if gjett in lite_alfabet:
        pos = int(lite_alfabet.find(gjett))
        gjett = alfabet[pos]
 
    if not gjett in alfabet:
        print("\nDu må gjette en BOKSTAV\n")
        time.sleep(1)
        continue
 
    if gjett in sjultord:
        print("\nDu har allerede gjettet " + gjett + "\n")
        time.sleep(1)
        continue
 
    if gjett in ord:
        print("riktig")
    else:
        antall_feil += 1
        print("feil")
        continue
 
    sjekk_sjultord = sjultord
    sjultord = ""
 
    for bokstav in ord:
        if bokstav in sjekk_sjultord:
            sjultord = sjultord + ord[len(sjultord)]
        else:
            sjultord = sjultord + sjekk_bokstav()
 
    if sjultord == ord:
        print_hangman()
        print("Du vant!")
        break