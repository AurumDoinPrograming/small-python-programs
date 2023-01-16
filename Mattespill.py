#bruk "pip3 install colorama" for at programe skal funke

from random import randint
import colorama #endrer fargen på "riktig eller feil"
#printer spiller regler og info
print('Mattespill. Det vil vises to tall og et svar, du skal gjette hvilken regneart som blir bruk for å få svaret. Svar med enten "+", "-", "*" eller "/" skriv "quit" for å avslutte.\n')


svar = 0
ganger_spilt = 0
riktig_gjettet = 0

while True: #for å få spillet til å repetere og kjøre på nytt.
    ganger_spilt += 1
#Velger to tilfeldige tall mellom 1-10 og en regneart.
    tall1 = randint(1, 10)
    tall2 = randint(1, 10)
    regneart = randint(1, 4)
#skjekker hvilken regneart som svaret hører til.
    if regneart == 1:
        svar = tall1 + tall2
    elif regneart == 2:
        svar = tall1 - tall2
    elif regneart == 3:
        svar = tall1 * tall2
    elif regneart == 4:
        svar = tall1 / tall2
#stiller spørsmålet og viser tallene.
    print(colorama.Fore.WHITE, str(tall1)  + " ? " + str(tall2) + "  =  " + str(svar))
    gjettetregneart = input('Hva er regnemåten?\n')


    if gjettetregneart == "+":
        gjettetsvar = tall1 + tall2
    elif gjettetregneart == "-":
        gjettetsvar = tall1 - tall2
    elif gjettetregneart == "*":
        gjettetsvar = tall1 * tall2
    elif gjettetregneart == "/":
        gjettetsvar = tall1 / tall2
    elif gjettetregneart == "quit":
        #gjør at det ikke teller med siste runde
        ganger_spilt -= 1 
        break
    else:
        #hvis man skriver et ugyldig svar taper man poeng
        print("skriv inn gyldig svar, du fikk ikke poeng for denne runden")
        continue

#forteller om svaret er riktig eller galt.
    if gjettetsvar == svar:
        riktig_gjettet += 1
        print(colorama.Fore.GREEN, "riktig")
    else:
        print(colorama.Fore.RED, "feil")
    print("Du har gjettet riktig ", riktig_gjettet, " ganger av totalt ", ganger_spilt, " ganger.")
prosent_riktig = riktig_gjettet / ganger_spilt * 100
print("Du stoppet spillet. du fikk ", riktig_gjettet, "av", ganger_spilt, ". Du fikk ", prosent_riktig, "% riktig.")
