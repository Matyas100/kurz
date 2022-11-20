from pojisteny import Pojisteny
from system import System
os = System()

while True:
    os.vypis_moznosti("Evidence Pojistěných")
    vyber = int(input())
    if vyber == 1:
        jmeno = input("Zadejte jméno pojištěného:\n").capitalize()
        prijmeni = input("Zadejte příjmení pojištěného:\n").capitalize()
        tcislo = int(input("Zadejte telefonní číslo:\n"))
        vek = int(input("Zadejte věk:\n"))
        pojisteny = Pojisteny(jmeno, prijmeni, tcislo, vek)
        pojisteny.pridej()
        os.data()

    elif vyber == 2:
        for jmena in pojisteny.ziskej():
            print(jmena)
        os.pokracuj()
    elif vyber == 3:
        jmeno = input("Zadejte jméno pojištěného:\n").capitalize()
        prijmeni = input("Zadejte příjmení pojištěného:\n").capitalize()
        pojisteny = pojisteny.ziskej_podle_jmena_a_prijmeni(jmeno, prijmeni)
        if (pojisteny == False):
            print("Uživatel neexistuje")
        else:
            print(pojisteny)
        os.pokracuj()
    elif vyber == 4:
        exit("Konec")